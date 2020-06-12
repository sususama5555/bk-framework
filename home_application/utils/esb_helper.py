# coding: utf-8
# @Time: 2019/10/16 10:00
# @Author: renpingsheng

import base64
import time

from blueking.component.shortcuts import get_client_by_user, get_client_by_request

count = 0


# 查询作业日志
def get_job_instance_log(request, task_id, biz_id):
    client = get_client_by_request(request)
    # 查询日志
    if get_job_instance_status(request, task_id, biz_id):
        resp = client.job.get_job_instance_log(
            job_instance_id=task_id,
            bk_biz_id=biz_id,
            bk_username='admin'
        )
        ip_logs = resp['data'][0]['step_results'][0]['ip_logs']
        return ip_logs
    else:
        return False


# 查询作业状态
def get_job_instance_status(request, task_id, biz_id):
    global count
    count += 1
    client = get_client_by_request(request)
    # 查询执行状态
    resp = client.job.get_job_instance_status(
        bk_username="root",
        bk_biz_id=biz_id,
        job_instance_id=task_id
    )
    if resp.get('data').get('is_finished'):
        count = 0
        return True
    elif not resp.get('data').get('is_finished') and count <= 5:
        time.sleep(2)
        return get_job_instance_status(request, task_id, biz_id)
    else:
        count = 0
        return False


# 执行作业
def execute_job(username, biz_id, bk_job_id, global_vars, steps, bk_callback_url):
    client = get_client_by_user(username)
    params = {
        "bk_username": username,
        "bk_biz_id": biz_id,
        "bk_job_id": bk_job_id,
        "steps": steps,
        # "global_vars": global_vars,
        "bk_callback_url": bk_callback_url
    }
    result = client.job.execute_job(**params)
    if result.get('result'):
        job_instance_id = result.get('data').get('job_instance_id')
        return True, job_instance_id
    else:
        return False, result.get('message')


################################################

# 快速执行脚本
def fast_execute_script(request, ip_list, biz_id, content):
    client = get_client_by_request(request)
    params = {
        'bk_username': "root",
        'bk_biz_id': int(biz_id),
        'script_content': base64.b64encode(content),
        'account': "root",
        'script_type': 1,
        'ip_list': ip_list,
    }
    resp = client.job.fast_execute_script(**params)
    if resp.get("result"):
        return resp.get('data').get('job_instance_id')


# 执行脚本并返回结果
def execute_script_and_return(request, ip_list, biz_id, content):
    """
    ip_list = [
        {"bk_cloud_id": 0, "ip": "192.168.36.137"},
        {"bk_cloud_id": 0, "ip": "192.168.148.117"},
    ]
    biz_id = 2
    content = "ls /opt"
    """
    job_instance_id = fast_execute_script(request, ip_list, biz_id, content)
    if job_instance_id:
        ip_logs = get_job_instance_log(request, job_instance_id, biz_id)
        return ip_logs
