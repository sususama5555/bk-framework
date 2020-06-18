# -*- coding: utf-8 -*-
"""
celery 任务示例

本地启动celery命令: python  manage.py  celery  worker  --settings=settings
周期性任务还需要启动celery调度命令：python  manage.py  celerybeat --settings=settings

pycharm配置
celery worker -l info
celery beat -l info
"""
import json
import datetime
import base64
from celery.task import task, periodic_task
from .host_and_monitor.models import HostInfo, hostMonitor

from blueking.component.shortcuts import get_client_by_user


# @periodic_task()
def get_loadreport():
    client = get_client_by_user('admin')
    script = "cat /proc/loadavg"
    # 1.63 0.61 0.22 1/228 2487
    # 1.63（1分钟平均负载） 0.61（5分钟平均负载） 0.22（15分钟平均负载） 1/228（分子是当前正在运行的进程数，分母是总的进程数） 2487（最近运行进程的ID）
    params = {
        "bk_biz_id": 2,
        "script_content": str(base64.b64encode(script.encode("utf-8"))),
        "account": "root",
        "ip_list": [
            {
                "bk_cloud_id": 0,
                "ip": "192.168.102.208"
            }
        ]
    }
    data = client.job.fast_execute_script(**params)
    return data


@periodic_task(run_every=datetime.timedelta(minutes=1))
def monitor_host():
    query = HostInfo.objects.filter(is_monitor="已监控")
    for host_info in query:
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
        client = get_client_by_user("admin")
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

        hostMonitor.objects.create(
            mem=execute_result_info["mem"],
            cpu=execute_result_info["cpu"],
            disk=execute_result_info["disk"],
            ip=host_info.ip,
        )