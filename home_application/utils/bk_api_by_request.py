# coding: utf-8
# @Time: 2019/10/16 10:00
# @Author: renpingsheng

import json
import base64
import requests

from config import APP_CODE, SECRET_KEY, BK_URL


################### 蓝鲸登录平台 #######################

def bk_login_get_all_users():
    """
    获取所有用户信息
    :return:
    """
    url = "{0}/api/c/compapi/v2/bk_login/get_all_users/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def bk_login_get_batch_users_platform_role():
    """
    批量获取用户各平台角色信息
    :return:
    """
    url = "{0}/api/c/compapi/v2/bk_login/get_batch_users_platform_role/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_username_list": ["szgd_tonysong", "szgd_renpingsheng"]
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def bk_login_get_batch_users():
    """
    批量获取用户信息
    :return:
    """
    url = "{0}/api/c/compapi/v2/bk_login/get_batch_users/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_username_list": ["szgd_tonysong", "szgd_renpingsheng"]
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def bk_login_get_user():
    """
    获取用户信息
    :return:
    """
    url = "{0}/api/c/compapi/v2/bk_login/get_user/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


################### 蓝鲸开发者中心 #######################


def bk_paas_get_app_info():
    """
    获取应用信息，支持批量获取
    :return:
    """
    url = "{0}/api/c/compapi/v2/bk_paas/get_app_info/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


################### 蓝鲸开发者中心 #######################


def cmsi_send_mail():
    """
    发送邮件
    :return:
    """
    url = "{0}/api/c/compapi/cmsi/send_mail/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "receiver__username": "szgd_renpingsheng",
        "title": "This is a Test mail",
        "content": "<html>Welcome to Blueking</html>",
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cmsi_send_sms():
    """
    发送短信
    :return:
    """
    url = "{0}/api/c/compapi/cmsi/send_sms/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "receiver": "18665373450",
        "receiver__username": "szgd_renpingsheng",
        "content": "Welcome to Blueking",
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cmsi_send_weixin():
    """
    发送微信消息，支持微信公众号消息，及微信企业号消息
    :return:
    """
    url = "{0}/api/c/compapi/cmsi/send_weixin/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "receiver": "18665373450",
        "receiver__username": "szgd_renpingsheng",
        "data": {
            "heading": "blueking alarm",
            "message": "This is a test.",
            "date": "2017-02-22 15:36",
            "remark": "This is a test!"
        }
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


################### 蓝鲸管控平台 #######################


def gse_get_agent_info():
    """
    查询agent心跳详细信息。数据非实时，延时1分钟内。
    :return:
    """
    url = "{0}/api/c/compapi/v2/gse/get_agent_info/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_id": 0,
        "hosts": [
            {
                "ip": "19.17.89.6",
                "bk_cloud_id": 0
            }
        ]
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def gse_get_agent_status():
    """
    查询agent实时在线状态
    :return:
    """
    url = "{0}/api/c/compapi/v2/gse/get_agent_status/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_id": 0,
        "hosts": [
            {
                "ip": "19.17.89.6",
                "bk_cloud_id": 0
            }
        ]
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


################### 蓝鲸标准运维 #######################

def sops_get_task_status():
    """
    查询任务或任务节点执行状态
    :return:
    """
    url = "{0}/api/c/compapi/v2/sops/get_task_status/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": "2",
        "task_id": "10"
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def sops_get_template_info():
    """
    查询业务下的单个模板详情
    :return:
    """
    url = "{0}/api/c/compapi/v2/sops/get_template_info/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": "2",
        "template_id": 2
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def sops_get_template_list():
    """
    查询业务下的模板列表
    :return:
    """
    url = "{0}/api/c/compapi/v2/sops/get_template_list/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 2
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def sops_operate_task():
    """
    操作任务，如开始、暂停、继续、终止等
    :return:
    """
    url = "{0}/api/c/compapi/v2/sops/operate_task/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "action": "start",  # start,pause,resume,revoke
        "bk_biz_id": "2",
        "task_id": "10"
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def sops_query_task_count():
    """
    查询任务实例分类统计总数
    conditions条件
        template_id	        string	        创建任务的模板ID
        name	            string	        任务名称
        creator	            string	        创建人
        create_time__gte	string	        任务创建时间起始时间,格式:2018-07-12 10:00:00
        create_time__lte	string	        任务创建时间截止时间,格式:2018-07-12 10:00:00
        executor	        string	        执行人
        start_time__gte	    string	        任务执行时间起始时间,格式:2018-07-12 10:00:00
        start_time__lte	    string	        任务执行时间截止时间,格式:2018-07-12 10:00:00
        is_started	        bool	        任务是否启动
        is_finished	        bool	        任务是否完成
    group_by
        flow_type           分类统计维度，
        status              按任务状态（未执行、执行中、已完成）统计，
        category            按照任务类型统计，
        flow_type           按照流程类型统计，
        create_method       按照创建方式
    :return:
    """
    url = "{0}/api/c/compapi/v2/sops/query_task_count/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": "2",
        # "conditions": {
        #     "create_time__lte": "2018-07-12 10:00:00",
        #     "is_started": True
        # },
        "group_by": "category"
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def sops_start_task():
    """
    开始执行任务
    :return:
    """
    url = "{0}/api/c/compapi/v2/sops/start_task/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": "2",
        "task_id": "10"
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def sops_create_task():
    """
    通过流程模板创建任务
    :return:
    """
    url = "{0}/api/c/compapi/v2/sops/create_task/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": "2",
        "template_id": "10",
        "flow_type": "10",
        "constants": {
            "${content}": "echo 1",
            "${params}": "",
            "${script_timeout}": 20
        }
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


################### 蓝鲸作业平台 #######################


def job_get_job_list():
    """
    查询作业模板
    :return:
    """
    url = "{0}/api/c/compapi/v2/job/get_job_list/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 2,
        # "creator": "admin",
        # "name": "test",
        # "create_time_start": "2016-02-22",
        # "create_time_end": "2016-02-22",
        # "last_modify_user": "admin",
        # "last_modify_time_start": "2016-02-22",
        # "last_modify_time_end": "2016-02-22",
        # "tag_id": "1",
        # "start": 0,
        # "length": 100
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def job_update_cron_status():
    """
    更新定时作业状态，如启动或暂停；操作者必须是业务的创建人或运维
    :return:
    """
    url = "{0}/api/c/compapi/v2/job/update_cron_status/".format(BK_URL)
    headers = {"Content-Type": "application/json; charset=utf-8"}
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 1,
        "cron_status": 1,
        "cron_id": 2
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def job_fast_push_file():
    """
    快速分发文件
    :return:
    """
    url = "{0}/api/c/compapi/v2/job/fast_push_file/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 2,
        "account": "root",
        "bk_callback_url": "xxxxxx",
        "file_target_path": "/tmp/[FILESRCIP]/",
        "file_source": [
            {
                "files": [
                    "/tmp/REGEX:[a-z]*.txt"
                ],
                "account": "root",
                "ip_list": [
                    {
                        "bk_cloud_id": 0,
                        "ip": "10.0.0.1"
                    },
                    {
                        "bk_cloud_id": 0,
                        "ip": "10.0.0.2"
                    }
                ],
                "custom_query_id": [
                    "3"
                ]
            }
        ],
        "ip_list": [
            {
                "bk_cloud_id": 0,
                "ip": "10.0.0.1"
            },
            {
                "bk_cloud_id": 0,
                "ip": "10.0.0.2"
            }
        ],
        "custom_query_id": [
            "3"
        ],
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def job_fast_execute_script():
    """
    快速执行脚本
    :return:
    """
    url = "{0}/api/c/compapi/v2/job/fast_execute_script/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 2,
        "script_id": 1,
        "script_content": base64.b64encode("cat /etc/redhat-release"),
        "script_param": "",
        "bk_callback_url": "http://dev.gdgov.cn:8000/call_back/",
        "script_timeout": 1000,
        "account": "root",
        "is_param_sensitive": 0,
        "script_type": 1,
        "ip_list": [
            {
                "bk_cloud_id": 0,
                "ip": "19.17.89.6"
            },
            {
                "bk_cloud_id": 0,
                "ip": "19.17.89.7"
            }
        ],
        "custom_query_id": [
            "3"
        ]
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def job_execute_job():
    """
    根据作业模板ID启动作业。支持全局变量，如果全局变量的类型为IP，参数值必须包含custom_query_id或ip_list。
    没有设置的参数将使用作业模版中的默认值。
    :return:
    """
    url = "{0}/api/c/compapi/v2/job/execute_job/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 2,
        "bk_job_id": 100,
        "global_vars": [
            {
                "id": 436,
                "custom_query_id": [
                    "3",
                    "5",
                    "7"
                ],
                "ip_list": [
                    {
                        "bk_cloud_id": 0,
                        "ip": "10.0.0.1"
                    },
                    {
                        "bk_cloud_id": 0,
                        "ip": "10.0.0.2"
                    }
                ]
            },
            {
                "id": 437,
                "value": "new String value"
            }
        ],
        "steps": [{
            "script_timeout": 1000,
            "script_param": "aGVsbG8=",
            "ip_list": [
                {
                    "bk_cloud_id": 0,
                    "ip": "10.0.0.1"
                },
                {
                    "bk_cloud_id": 0,
                    "ip": "10.0.0.2"
                }
            ],
            "custom_query_id": [
                "3"
            ],
            "script_id": 1,
            "script_content": "ZWNobyAkMQ==",
            "step_id": 200,
            "account": "root",
            "script_type": 1
        },
            {
                "script_timeout": 1003,
                "ip_list": [
                    {
                        "bk_cloud_id": 0,
                        "ip": "10.0.0.1"
                    },
                    {
                        "bk_cloud_id": 0,
                        "ip": "10.0.0.2"
                    }
                ],
                "custom_query_id": [
                    "3"
                ],
                "script_id": 1,
                "script_content": "ZWNobyAkMQ==",
                "step_id": 1,
                "db_account_id": 31
            },
            {
                "file_target_path": "/tmp/[FILESRCIP]/",
                "file_source": [
                    {
                        "files": [
                            "/tmp/REGEX:[a-z]*.txt"
                        ],
                        "account": "root",
                        "ip_list": [
                            {
                                "bk_cloud_id": 0,
                                "ip": "10.0.0.1"
                            },
                            {
                                "bk_cloud_id": 0,
                                "ip": "10.0.0.2"
                            }
                        ],
                        "custom_query_id": [
                            "3"
                        ]
                    }
                ],
                "ip_list": [
                    {
                        "bk_cloud_id": 0,
                        "ip": "10.0.0.1"
                    },
                    {
                        "bk_cloud_id": 0,
                        "ip": "10.0.0.2"
                    }
                ],
                "custom_query_id": [
                    "3"
                ],
                "step_id": 2,
                "account": "root"
            }
        ]
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def job_get_cron_list():
    """
    查询业务下定时作业信息
    :return:
    """
    url = "{0}/api/c/compapi/v2/job/get_cron_list/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 2,
        # "cron_name": "test",
        # "cron_id": 1,
        # "cron_status": 1,
        # "creator": "admin",
        # "create_time_start": "2018-03-02",
        # "create_time_end": "2018-03-23",
        # "last_modify_user": "admin",
        # "last_modify_time_start": "2018-03-02",
        # "last_modify_time_end": "2018-03-23",
        # "start": 0,
        # "length": 100
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def job_get_job_instance_status():
    """
    根据作业实例 ID 查询作业执行状态
    :return:
    """
    url = "{0}/api/c/compapi/v2/job/get_job_instance_status/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 2,
        "job_instance_id": 100
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def job_get_job_instance_log():
    """
    根据作业实例ID查询作业执行日志
    :return:
    """
    url = "{0}/api/c/compapi/v2/job/get_job_instance_log/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 2,
        "job_instance_id": 100
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def job_get_job_detail():
    """
    根据作业模板ID查询作业模板详情
    :return:
    """
    url = "{0}/api/c/compapi/v2/job/get_job_detail/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 2,
        "bk_job_id": 1089
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def job_get_own_db_account_list():
    """
    查询用户有权限的DB帐号列表
    :return:
    """
    url = "{0}/api/c/compapi/v2/job/get_own_db_account_list/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 2,
        "start": 0,
        "length": 100
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def job_save_cron():
    """
    新建或保存定时作业；
    新建定时作业，作业状态默认为暂停；
    操作者必须是业务的创建人或运维
    :return:
    """
    url = "{0}/api/c/compapi/v2/job/save_cron/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 1,
        "bk_job_id": 100,
        "cron_name": "test",
        "cron_expression": "0 0/5 * * * ls"
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")
