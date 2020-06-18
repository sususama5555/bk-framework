# -*- coding: utf-8 -*-
import os
import copy
import json
import base64
import time
import datetime
import requests

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.context import Context
from django.utils.encoding import escape_uri_path

from blueking.component.shortcuts import get_client_by_user, get_client_by_request
# 跨域！
from django.views.decorators.csrf import csrf_exempt
# from django.template import Context, Template

from .host_and_monitor.models import HostInfo
from .models import Template
from .models import Task
from .models import FileInfo


# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
# 页面跳转
def host_list(request):
    """
    首页
    """
    return render(request, 'home_application/host_and_monitor/host_list.html')


def report(request):
    id = request.GET.get("id")
    return render(request, 'home_application/host_and_monitor/report.html', {"id": id})


def backup(request):
    return render(request, 'home_application/backup_and_log/topo.html')


def backup_log(request):
    return render(request, 'home_application/backup_and_log/backup_log.html')


def dev_guide(request):
    """
    开发指引
    """
    return render(request, 'home_application/dev_guide.html')


def contact(request):
    """
    联系页
    """
    return render(request, 'home_application/contact.html')



def report_link(request):
    id = request.GET.get("id")
    return render(request, 'home_application/program/report.html', {"id": id})


# =======================业务代码==========================

def test(request):
    # return JsonResponse({"uesrname": request.user.username, "result": "OK"})
    return render(request, 'home_application/program/report.html', {"testSpan": "我是测试"})


def connect_bak(request):
    request.POST.get("id", 0)
    data = "链接成功"
    return HttpResponse(json.dumps({"data": data}))


def get_biz_topo(request):
    biz_info = request.GET.get("biz", 2)
    bk_biz_id = biz_info.split(":")[0]
    # client = get_client_by_user("admin")
    client = get_client_by_request(request)
    topo_data = client.cc.search_biz_inst_topo(**{"bk_biz_id": bk_biz_id})
    topo_list = topo_data["data"]
    topo_list_build = str(topo_list).replace("bk_inst_name", "label").replace("child", "children")
    return JsonResponse({"result": True, "data": eval(topo_list_build)})


def get_topo_host(request):
    """根据拓扑节点获取主机"""
    params = json.loads(request.body)
    # client = get_client_by_user("admin")
    client = get_client_by_request(request)
    kwargs = {
        "condition": [
            {
                "bk_obj_id": params["bk_obj_id"],
                "fields": [],
                "condition": [
                    {
                        "field": "bk_" + params["bk_obj_id"] + "_id",
                        "operator": "$eq",
                        "value": params["bk_inst_id"]
                    }
                ]
            }
        ]
    }
    data = client.cc.search_host(**kwargs)
    bk_host_innerips = []
    if data.get('result', False):
        for info in data['data']['info']:
            bk_host_innerips.append({"ip": info['host']['bk_host_innerip']})

    host_list = ["{}".format(ip["ip"]) for ip in bk_host_innerips]
    return JsonResponse({"result": True, "data": ";\n".join(host_list)})


def search_biz(request):
    # 查询业务
    biz_list = []
    # client = get_client_by_user('admin')
    client = get_client_by_request(request)
    biz_result = client.cc.search_business()
    for biz in biz_result["data"]["info"]:
        biz_list.append({"id": biz["bk_biz_id"], "name": biz["bk_biz_name"]})

    return JsonResponse({"result": True, "data": biz_list})



def search_host(request):
    # 查询主机
    biz_id = request.GET["biz"].split(":")[0]
    host_list = []
    # client = get_client_by_user('admin')
    client = get_client_by_request(request)
    params = {
        "bk_biz_id": int(biz_id)
    }
    host_result = client.cc.search_host(**params)
    for biz in host_result["data"]["info"]:
        host_list.append({"id": biz["host"]["bk_host_id"], "innerip": biz["host"]["bk_host_innerip"]})

    return JsonResponse({"data": host_list})


# @csrf_exempt
def add_host(request):
    params = json.loads(request.body)
    innerip = params["innerip"]
    business = params["biz"]
    if HostInfo.objects.filter(ip=innerip).exists():
        return JsonResponse({"result": False, "data": "请勿重复添加".format(innerip)})
    # client = get_client_by_user('admin')
    client = get_client_by_request(request)
    params = {
        "ip": {
            "data": [innerip],
            "exact": 1,
            "flag": "bk_host_innerip|bk_host_outerip"
        },
    }
    host_result = client.cc.search_host(**params)
    host_info = host_result["data"]["info"][0]["host"]

    HostInfo.objects.create(ip=host_info["bk_host_innerip"], name=host_info["bk_host_name"],
                            business=business, cloud_area=host_info["bk_cloud_id"][0]["bk_inst_name"],
                            os=host_info["bk_os_name"])
    return JsonResponse({"result": 1, "data": host_result})


def init_host_table(request):
    host_data = HostInfo.objects.all()
    table_data = []
    for item in host_data:
        table_data.append({
            "id": item.id,
            "ip": item.ip,
            "name": item.name,
            "business": item.business.split(":")[-1],
            "cloud_area": item.cloud_area,
            "os": item.os
        })

    return JsonResponse({"result": True, "data": table_data})


def delete_host(request):
    row_id = request.GET["row_id"]
    HostInfo.objects.get(id=row_id).delete()

    return JsonResponse({"result": True})


def detail_report(request):
    data = {
        "title": {
            "text": 'ECharts 入门示例'
        },
        "tooltip": {},
        "legend": {
            "data": ['销量']
        },
        "xAxis": {
            "data": ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
        },
        "yAxis": {},
        "series": [{
            "name": '销量',
            "type": 'bar',
            "data": [5, 20, 36, 10, 10, 20]
        }]
    }

    # host_id = request.GET["id"]

    return JsonResponse({"result": True, "data": data})


def search_file(request):
    host_area = json.loads(request.body)["host"]
    file_path = json.loads(request.body)["path"]
    file_tail = json.loads(request.body)["tail"]
    bk_biz_id = json.loads(request.body).get("biz_id", 2).split(":")[0]

    host_list = host_area.split(";\n")
    ip_list = [{"bk_cloud_id": 0, "ip": ip} for ip in host_list]
    # script = '''#!/bin/bash
    # cd {} || return
    # find . -name "*{}" | sed "s;./;;g" | wc -l
    # find . -name "*{}" | sed "s;./;;g"| xargs du -ck
    # '''.format(file_path, file_tail, file_tail)
    # 统计当前目录及子目录
    # script = '''#!/bin/bash
    #     cd {0} || return
    #     find . -name "*{1}" | wc -l
    #     find . -name "*{1}" | xargs du -ck
    #     '''.format(file_path, file_tail)
    # 统计当前目录 不包括子目录文件
    script = '''#!/bin/bash
           cd {0} || return
           find *{1} | wc -l
           find *{1} | xargs du -ck
           '''.format(file_path, file_tail)
    encode_str = base64.b64encode(script.encode("utf-8"))
    script_content = str(encode_str, 'utf-8')
    kwargs = {
        "bk_biz_id": bk_biz_id,
        "ip_list": ip_list,
        "script_content": script_content,
        "account": "root",
    }
    # client = get_client_by_user("admin")
    client = get_client_by_request(request)
    data = client.job.fast_execute_script(**kwargs)
    job_instance_id = data["data"]["job_instance_id"]

    kwargs_log = {
        "bk_biz_id": bk_biz_id,
        "job_instance_id": job_instance_id
    }
    polling_result = True
    while polling_result:
        job_log = client.job.get_job_instance_log(**kwargs_log)
        for re in job_log['data']:
            if re['is_finished']:
                polling_result = False

        # 处理数据
    execute_result_info = []
    for re in job_log['data']:
        for res in re['step_results']:
            tmp_dict = {}
            for resu in res['ip_logs']:
                tmp_dict['ip'] = resu['ip']
                if "No such file or directory" in resu['log_content']:
                    break
                strs = str(resu['log_content']).split("\n")
                bk_cloud_id = resu['bk_cloud_id']
                if strs[0] == '0':
                    break
                tmp_dict['number'] = strs[0]
                string = ''
                if len(strs) >= 2:
                    for cnt in range(1, len(strs) - 2):
                        # 1.文件名:./data/bkce/xxxxx
                        # string = string + ";" + strs[cnt].split()[1]
                        # 2.文件名:xxxxx
                        string = string + ";" + strs[cnt].split()[-1]
                    tmp_dict['bk_cloud_id'] = bk_cloud_id
                    tmp_dict['file_list'] = string[1: len(string)]
                    tmp_dict['size'] = strs[len(strs) - 2].split()[0] + "KB"
                    execute_result_info.append(copy.deepcopy(tmp_dict))
                    tmp_dict.clear()

    return JsonResponse({"result": True, "data": execute_result_info})


def back_up(request):
    """打包备份文件"""
    params = json.loads(request.body)
    # 快速执行脚本的内容
    bk_biz_id = 2
    # backup_dir = "/tmp/test/backup" # 可指定备份路径
    ip_list = [{"bk_cloud_id": params["row"]["bk_cloud_id"], "ip": params["row"]["ip"]}]
    script = '''#! /bin/bash
       cd {0} || return
       t=$(date +%Y%m%d%H%M%S)
       tar -zcf {0}/bkds$t.tar.gz  $1
       echo bkds$t.tar.gz '''.format(params["path"])
    # script = '''#! /bin/bash
    # cd {0} || return
    # t=$(date +%Y%m%d%H%M%S)
    # for i in $1
    # do
    # tar -zcf {1}/$i-$t.tar.gz $i
    # echo $i-$t.tar.gz
    # done'''.format(params["path"], backup_dir)
    encode_str = base64.b64encode(script.encode("utf-8"))
    script_content = str(encode_str, 'utf-8')

    # 脚本的参数
    pattern = params["row"]["file_list"]
    pattern = "\t".join(pattern.split(";"))
    args = base64.b64encode(pattern.encode('utf-8'))
    script_param = str(args, 'utf-8')
    kwargs = {
        "bk_biz_id": bk_biz_id,
        "ip_list": ip_list,
        "script_content": script_content,
        "account": "root",
        "script_param": script_param,
    }
    # client = get_client_by_user("admin")
    client = get_client_by_request(request)
    tar_result = client.job.fast_execute_script(**kwargs)

    # 获取脚本执行日志
    job_instance_id = tar_result["data"]["job_instance_id"]

    kwargs_log = {
        "bk_biz_id": bk_biz_id,
        "job_instance_id": job_instance_id
    }
    polling_result = True
    log_content = []
    while polling_result:
        job_log = client.job.get_job_instance_log(**kwargs_log)
        for re in job_log['data']:
            if re['is_finished']:
                polling_result = False
                for tmp in re["step_results"]:
                    log_content.append(tmp["ip_logs"][0]["log_content"])

    back_up_info = FileInfo(
        ip=params["row"]["ip"],
        path=params["path"],
        number=params["row"]["number"],
        file_list=params["row"]["file_list"],
        size=params["row"]["size"],
        creater=request.user.username,
    )
    back_up_info.save()

    return JsonResponse({"result": True, "data": "已备份至" + params["path"] + "/" + ";\n".join(log_content)})


def get_backup_log_table(request):
    """获取备份历史表格"""
    table = [i.to_dict() for i in FileInfo.objects.all()]
    return JsonResponse({"result": True, "data": table})


# 以下是6.6模拟题代码：
def task(request):
    """
    首页
    """
    return render(request, 'home_application/exam0606/task.html')


def template(request):
    # id = request.GET.get("id")
    return render(request, 'home_application/exam0606/template.html')


def api_test(request):
    data = {}
    if request.GET:
        a_key = list(request.GET)[0]
        b_key = list(request.GET)[1]
        a_value = request.GET.get(a_key)
        b_value = request.GET.get(b_key)
        data = {a_key: a_value, b_key: b_value}
    return JsonResponse({"result": True, "message": "success", "data": data})


def init_template(request):
    biz_list = []
    # client = get_client_by_user('admin')
    client = get_client_by_request(request)
    biz_result = client.cc.search_business()
    for biz in biz_result["data"]["info"]:
        biz_list.append({"id": biz["bk_biz_id"], "name": biz["bk_biz_name"]})

    return JsonResponse({"data": biz_list})


def add_template(request):
    params = json.loads(request.body)
    creator = request.user.username
    Template.objects.create(business=params["biz"], type=params["type"], name=params["name"], creator=creator,
                            updator="")
    return JsonResponse({"result": True})


def init_table(request):
    query_data = Template.objects.all()
    table_data = []
    for item in query_data:
        table_data.append({
            "id": item.id,
            "name": item.name,
            "business": item.business,
            "type": item.type,
            "creator": item.creator,
            "create_at": item.create_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updator": item.updator,
            "update_at": item.create_at.strftime("%Y-%m-%d %H:%M:%S"),
        })

    return JsonResponse({"result": True, "data": table_data})


def delete_template(request):
    row_id = request.GET["row_id"]
    Template.objects.get(id=row_id).delete()

    return JsonResponse({"result": True})


def edit_template(request):
    params = json.loads(request.body)
    data = Template.objects.get(id=params["row_id"])
    data.type = params["type"]
    data.name = params["name"]
    data.business = params["business"]
    data.updator = request.user.username
    data.save()
    return JsonResponse({"result": True})


def search_template(request):
    params = request.GET
    query_data = Template.objects.all()
    if params["name"]:
        query_data = query_data.filter(
            name__contains=params["name"]
        )
    if params["type"]:
        query_data = query_data.filter(
            type=params["type"]
        )
    if params["biz"]:
        query_data = query_data.filter(
            business=params["biz"]
        )
    table_data = []
    for item in query_data:
        table_data.append({
            "id": item.id,
            "name": item.name,
            "business": item.business,
            "type": item.type,
            "creator": item.creator,
            "create_at": item.create_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updator": item.updator,
            "update_at": item.create_at.strftime("%Y-%m-%d %H:%M:%S"),
        })

    return JsonResponse({"result": True, "data": table_data})


def add_task(request):
    params = json.loads(request.body)
    creator = request.user.username
    Task.objects.create(business=params["biz"], type=params["type"], name=params["name"], symbol=params["symbol"],
                        template=params["template"],
                        creator=creator)
    return JsonResponse({"result": True})


def init_task(request):
    query_data = Task.objects.all()
    table_data = []
    for item in query_data:
        table_data.append({
            "id": item.id,
            "name": item.name,
            "business": item.business,
            "type": item.type,
            "creator": item.creator,
            "create_at": item.create_at.strftime("%Y-%m-%d %H:%M:%S"),
            "symbol": item.symbol,
            "template": item.template,
        })

    return JsonResponse({"result": True, "data": table_data})


def check_upload_wrapper(func):
    def inner(*args, **kwargs):
        if not os.path.exists("upload/"):
            os.makedirs("upload/")
        return func(*args, **kwargs)

    return inner


@csrf_exempt
@check_upload_wrapper
def upload_template(request):
    file_obj = request.FILES.get('file')  # 获取上传的文件对象
    t = time.strftime('%Y%m%d%H%M%S')
    now_file_name = t + '.' + file_obj.name.split('.')[-1]  # 得到文件在后台的保存名字
    file_path = os.path.join('upload', now_file_name)
    with open(file_path, "wb") as f:
        for line in file_obj.chunks():
            f.write(line)
    return JsonResponse({'result': True, 'data': file_path})


def download_template(request):
    file_name = u"checklist.xls"
    file_path = os.path.join("upload/sample_temp", file_name)
    file = open(file_path, 'rb')
    response = HttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = "attachment;filename*=utf-8''{}".format(escape_uri_path(file_name))
    return response


# 备份记录
def init_backup_log_table(request):
    FileInfo.objects.get()