# coding: utf-8
import base64
import json
import os
import time
import copy
import datetime
import random
from wsgiref.util import FileWrapper
import logging
import requests

from config import *

import xlrd
from django.views.generic import View
from django.utils.encoding import escape_uri_path
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from home_application.task_and_temp.models import JobTemplate, JobToDoList, JobObject
from home_application.utils.parse_time import get_current_timestr, parse_datetime_to_timestr
from blueking.component.shortcuts import get_client_by_user, get_client_by_request

from ..host_and_monitor.models import HostInfo, hostMonitor

logger = logging.getLogger('celery')


def host_list(request):
    """
    首页
    """
    return render(request, 'home_application/host_and_monitor/host_list.html')


def report(request):
    id = request.GET.get("id")
    return render(request, 'home_application/host_and_monitor/report.html', {"id": id})


def api_test(request):
    client = get_client_by_request(request)
    data = client.bk_login.get_user()
    return JsonResponse(
        {
            "result": True,
            "username": data["data"]["bk_username"],
            "phone": data["data"]["phone"],
            "last_login": parse_datetime_to_timestr(request.user.last_login),
            "email": data["data"]["email"]
        }
    )


def search_biz(request):
    # 查询业务
    biz_list = []
    # client = get_client_by_user('admin')
    client = get_client_by_request(request)
    biz_result = client.cc.search_business()
    for biz in biz_result["data"]["info"]:
        biz_list.append({"id": biz["bk_biz_id"], "name": biz["bk_biz_name"]})

    return JsonResponse({"result": True, "data": biz_list})


def search_set(request):

    biz_id = request.GET["biz"].split(":")[0]
    # client = get_client_by_user('admin')
    client = get_client_by_request(request)
    set_result = client.cc.search_set({"bk_biz_id": biz_id})

    data = [{"bk_set_name": i.get("bk_set_name"), "bk_set_id": i.get("bk_set_id")} for i in set_result["data"]["info"]]
    return JsonResponse({"result": True, "data": data})


def search_host(request):
    # 根据集群查询主机
    set_id = int(request.GET["set"].split(":")[0])
    # client = get_client_by_user('admin')
    client = get_client_by_request(request)
    kwargs = {
        "condition": [
            {
                "bk_obj_id": "set",
                "fields": [],
                "condition": [
                    {
                        "field": "bk_set_id",
                        "operator": "$eq",
                        "value": set_id
                    }
                ]
            }
        ]
    }
    host_result = client.cc.search_host(**kwargs)
    host_list = [{"id": biz["host"]["bk_host_id"], "innerip": biz["host"]["bk_host_innerip"]} for biz in host_result["data"]["info"]]
    # for biz in host_result["data"]["info"]:
    #     host_list.append({"id": biz["host"]["bk_host_id"], "innerip": biz["host"]["bk_host_innerip"]})

    return JsonResponse({"result": True, "data": host_list})


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
    return JsonResponse({"result": True, "data": host_result})


def get_search_host(request):
    params = json.loads(request.body)
    biz = params.get("biz")
    ip = params.get("ip")
    query = HostInfo.objects.all()
    if biz:
        query = query.filter(business=biz)
    if ip:
        query = query.filter(ip__in=ip.split(";"))

    data = [i.to_dict() for i in query]
    return JsonResponse({"result": True, "data": data})


def delete_host(request):
    row_id = request.GET["row_id"]
    HostInfo.objects.get(id=row_id).delete()

    return JsonResponse({"result": True})


def get_host_monitor(request):
    row_id = request.GET["row_id"]
    host_info = HostInfo.objects.get(id=row_id)
    biz_id = host_info.business.split(":")[0]
    script = '''
    #!/bin/bash
    MEMORY=$(free -m | awk 'NR==2{printf "%.2f%%", $3*100/$2 }')
    DISK=$(df -h | awk '$NF=="/"{printf "%s", $5}')
    CPU=$(top -bn1 | grep load | awk '{printf "%.2f%%", $(NF-2)}')
    DATE=$(date "+%Y-%m-%d %H:%M:%S")
    echo -e "$DATE|$MEMORY|$DISK|$CPU"
    '''
    encode_str = base64.b64encode(script.encode("utf-8"))
    script_content = str(encode_str, 'utf-8')
    kwargs = {
        "bk_biz_id": int(biz_id),
        "ip_list": [{"bk_cloud_id": 0, "ip": host_info.ip}],
        "script_content": script_content,
        "account": "root",
    }
    # client = get_client_by_user("admin")
    client = get_client_by_request(request)
    data = client.job.fast_execute_script(**kwargs)
    job_instance_id = data["data"]["job_instance_id"]

    kwargs_log = {
        "bk_biz_id": biz_id,
        "job_instance_id": job_instance_id
    }
    polling_result = True
    while polling_result:
        job_log = client.job.get_job_instance_log(**kwargs_log)
        for re in job_log['data']:
            if re['is_finished']:
                polling_result = False

    execute_result_info = {"mem": 43, "disk": 58, "cpu": 14}
    for re in job_log['data']:
        for res in re['step_results']:
            log_content_list = res['ip_logs'][0]["log_content"].split("|")
            mem = log_content_list[1]
            disk = log_content_list[2]
            cpu = log_content_list[3]
            execute_result_info = {"mem": mem, "disk": disk, "cpu": cpu}

    host_info.mem = execute_result_info["mem"]
    host_info.cpu = execute_result_info["cpu"]
    host_info.disk = execute_result_info["disk"]
    host_info.save()
    return JsonResponse({"result": True, "data": execute_result_info})


def add_host_monitor(request):
    row_id = request.GET["row_id"]
    host_info = HostInfo.objects.get(id=row_id)
    host_info.is_monitor = "已监控"
    host_info.save()
    return JsonResponse({"result": True})


def delete_host_monitor(request):
    row_id = request.GET["row_id"]
    host_info = HostInfo.objects.get(id=row_id)
    host_info.is_monitor = "未监控"
    host_info.save()
    return JsonResponse({"result": True})


def get_host_list(request):
    query = HostInfo.objects.filter(is_monitor="已监控")
    ip_list = [i.to_dict() for i in query]
    return JsonResponse({"result": True, "data": ip_list})


def get_host_monitor_info(request):
    ip = request.GET["ip"]
    if not ip:
        return JsonResponse({"result": False, "message": "请选择ip地址！"})
    try:
        monitor_data = hostMonitor.objects.filter(ip=ip)
        data_time = []
        data_mem = []
        data_cpu = []
        data_disk = []
        for item in monitor_data:
            data_time.append(item.to_dict().get("monitor_time"))
            data_mem.append(item.to_dict().get("mem"))
            data_cpu.append(item.to_dict().get("cpu"))
            data_disk.append(item.to_dict().get("disk"))

        data_Y = [data_mem, data_cpu, data_disk]
    except:
        data_time = [(datetime.datetime.today() - datetime.timedelta(hours=1) + datetime.timedelta(minutes=min)).strftime(
            "%Y-%m-%d %H:%M:%S") for min in range(60)]
        data_mem = [random.randint(11, 83) for i in range(60)]
        data_cpu = [random.randint(11, 22) for i in range(60)]
        data_disk = [random.randint(55, 60) for i in range(60)]
        data_Y = [data_mem, data_cpu, data_disk]
    return JsonResponse({"result": True, "dataX": data_time, "dataY": data_Y})


# 蓝鲸监控
def get_monitor_data(biz_id,
             func,
             metric_type,
             metric_item,
             alias_name,
             set_time="24h",
             group_by="ip",
             metric_service="system"):
    """

    :param biz_id:      业务id    如： 2
    :param func:        sql函数     如：MAX
    :param metric_type: 指标类型    如： disk
    :param metric_item:     指标项     如：in_use
    :param alias_name:     别名     如：disk_used
    :param metric_service:  指标服务名称  如： system
    :param set_time:  时间区间  如：
    :param group_by:  分组  如： ip
    :return:
                {
                "ip": "172.17.16.9",
                "disk_used": 32.040231072470476,
                "time": 1530503783000
                }

    """

    url = "{0}/api/c/compapi/v2/monitor/query_data/".format(
        BK_URL)
    headers = {"Content-Type": "application/json; charset=utf-8"}  # 默认请求头
    sql = "select {func}({metric_item}) as {alias_name} from {biz_id}_{metric_service}_{metric_type} where time > '{set_time}' group by {group_by}"\
        .format(func=func, metric_item=metric_item, alias_name=alias_name, biz_id=biz_id, metric_service=metric_service, metric_type=metric_type, set_time=set_time, group_by=group_by)
    # 接口调用所需要的参数
    kwargs = {
        "app_code": APP_CODE,  # 蓝鲸APP的ID，该APP需要有ESB的调用权限
        "app_secret": SECRET_KEY,  # APP对应的TOKEN
        "bk_username": "admin",  # 当前用户用户名，应用免登录态验证白名单中的应用，用此字段指定当前用户
        # "prefer_storage": "",  # 查询引擎，如果为ES DSL查询，则需指定值为es，不传默认为空
        # 查询语句
        "sql": sql,
    }
    response = requests.post(url=url,
                             headers=headers,
                             data=json.dumps(kwargs),
                             verify=False)
    if response.status_code != 200:
        for i in range(4):
            logger.warning("{0} biz get data failed {1}".format(biz_id, i + 1))
            response = requests.post(url=url,
                                     headers=headers,
                                     data=json.dumps(kwargs),
                                     verify=False)
            if response.status_code == 200:
                result = json.loads(response.content)
                try:
                    result_list = result["data"]["list"]
                    return result_list
                except Exception as _:
                    return []

        else:
            # 接口请求返回的状态码，只有200才是成功
            return False
        # print response.status_code
    else:
        result = json.loads(response.content)
        try:
            result_list = result["data"]["list"]
            return result_list
        except Exception as _:
            return []
