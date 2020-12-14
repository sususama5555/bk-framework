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

from config import BK_JOB_URL
from blueking.component.shortcuts import get_client_by_user, get_client_by_request
# 跨域！
from django.views.decorators.csrf import csrf_exempt
# from django.template import Context, Template
from .models import BackupLog


# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
# 页面跳转

def backup(request):
    return render(request, 'home_application/backup_and_log/backup.html')


def backup_log(request):
    return render(request, 'home_application/backup_and_log/backup_log.html')

# =======================业务代码==========================


def get_biz_topo(request):
    biz_info = request.GET.get("biz", 2)
    bk_biz_id = biz_info.split(":")[0]
    client = get_client_by_request(request)
    topo_data = client.cc.search_biz_inst_topo(**{"bk_biz_id": bk_biz_id})
    topo_list = topo_data["data"]
    return JsonResponse({"result": True, "data": topo_list})


def get_topo_host(request):
    """根据拓扑节点获取主机"""
    params = json.loads(request.body)
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


def get_checked_topo_host(request):
    """根据拓扑节点获取主机(多选拓扑)"""
    params = json.loads(request.body)
    checked_nodes = params.get("checkedNodes")
    module_checked = [i.get("bk_inst_id") for i in checked_nodes if i.get("bk_obj_id") == "module"]
    client = get_client_by_request(request)
    kwargs = {
        "condition": [
            {
                "bk_obj_id": "module",
                "fields": [],
                "condition": [
                    {
                        "field": "bk_module_id",
                        "operator": "$in",
                        "value": module_checked
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
    client = get_client_by_user("admin")
    # client = get_client_by_request(request)
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

    back_up_info = BackupLog(
        ip=params["row"]["ip"],
        path=params["path"],
        number=params["row"]["number"],
        file_list=params["row"]["file_list"],
        size=params["row"]["size"],
        creater=request.user.username,
        job_instance_id=job_instance_id,
        job_link="{job_url}/?taskInstanceList&appId={biz_id}#taskInstanceId={job_id}".format(
            job_url=BK_JOB_URL, biz_id=bk_biz_id, job_id=job_instance_id),
    )
    back_up_info.save()

    return JsonResponse({"result": True, "data": "已备份至" + params["path"] + "/" + ";\n".join(log_content)})


def get_backup_log_table(request):
    """获取备份历史表格"""
    table = [i.to_dict() for i in BackupLog.objects.all()]
    return JsonResponse({"result": True, "data": table})


# 备份记录
def init_backup_log_table(request):
    BackupLog.objects.get()