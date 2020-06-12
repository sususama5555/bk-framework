# coding: utf-8
# @Time: 2019/10/16 17:01
# @Author: renpingsheng

import base64

from blueking.component.shortcuts import get_client_by_request, get_client_by_user


################### 蓝鲸登录平台 #######################

# 获取所有用户信息
def bk_login_get_all_users(request):
    client = get_client_by_request(request)
    res = client.bk_login.get_all_users()
    if res.get('code') == 0:
        return res.get('data')


# 批量获取用户信息
def bk_login_get_batch_users(request, user_list):
    client = get_client_by_request(request)
    params = {"bk_username_list": user_list}
    res = client.bk_login.get_batch_users(**params)
    if res.get('code') == 0:
        return res.get('data')


# 获取用户信息
def bk_login_get_user(request):
    client = get_client_by_request(request)
    res = client.bk_login.get_user()
    if res.get('code') == 0:
        return res.get('data')


################### 蓝鲸开发者中心 #######################

# 获取应用信息
def bk_paas_get_app_info(request):
    client = get_client_by_request(request)
    res = client.bk_paas.get_app_info()
    if res.get('code') == 0:
        return res.get('data')


################### 蓝鲸开发者平台 #######################

# 发送邮件
def cmsi_send_mail(request):
    client = get_client_by_request(request)
    params = {
        'bk_username': 'admin',
        "receiver__username": "szgd_renpingsheng",
        "title": "This is a Test",
        "content": "<html>Welcome to Blueking</html>",
    }
    res = client.cmsi.send_mail(**params)
    if res.get('result') == 0:
        return True
    return False


# 发送邮件
def cmsi_send_sms(request):
    client = get_client_by_request(request)
    params = {
        'bk_username': 'admin',
        "receiver__username": "szgd_renpingsheng",
        "content": "<html>Welcome to Blueking</html>",
    }
    res = client.cmsi.send_sms(**params)
    if res.get('result') == 0:
        return True
    return False


################### 蓝鲸管控平台 #######################

# 查询agent心跳详细信息。数据非实时，延时1分钟内。
def gse_get_agent_info(request):
    client = get_client_by_request(request)
    params = {
        "bk_supplier_account": "0",
        "hosts": [
            {
                "ip": "192.168.148.103",
                "bk_cloud_id": 0
            }
        ]
    }
    res = client.gse.get_agent_info(**params)
    if res.get('code') == 0:
        return res.get('data')
    return res["message"]


# 查询agent实时在线状态
def gse_get_agent_status(request):
    client = get_client_by_request(request)
    params = {
        "bk_supplier_account": "0",
        "hosts": [
            {
                "ip": "192.168.148.114",
                "bk_cloud_id": 0
            }
        ]
    }
    res = client.gse.get_agent_status(**params)
    if res.get('code') == 0:
        return res.get('data')
    return res["message"]


################### 蓝鲸作业平台 #######################

# 获取所有作业
def job_get_job_list(request):
    client = get_client_by_request(request)
    params = {
        "bk_biz_id": 2,  # 业务ID
        # "name": "更新",     # 作业名称，模糊匹配
        # "creator": "szgd_gavinlin",   # 作业创建人帐号
        # "create_time_start": "2019-01-16",  # 创建起始时间，YYYY-MM-DD格式
        # "create_time_end": "2019-01-16",  # 创建结束时间，YYYY-MM-DD格式
        # "last_modify_user": "v_leehe",     # 作业修改人帐号
        # "last_modify_time_start": "2019-01-17",   # 最后修改起始时间，YYYY-MM-DD格式
        # "last_modify_time_end": "2019-01-17",     # 最后修改结束时间，YYYY-MM-DD格式
        # "tag_id": "1",       # 作业标签ID，1.未分类、2.运营发布、3.故障处理、4.常用工具、5.产品自助、6.测试专用、7.持续集成
        # "start": "1",        # 默认0表示从第1条记录开始返回
        # "length": "1",       # 返回记录数量，不传此参数默认返回全部
    }
    res = client.job.get_job_list(**params)

    if res.get('code') == 0:
        return res.get('data')


# 根据作业模板ID查询作业模板详情,测试OK
def job_get_job_detail(request):
    client = get_client_by_request(request)
    params = {
        "bk_biz_id": 2,
        "bk_job_id": 1135,  # 通过 job_get_job_list 接口查询
    }
    res = client.job.get_job_detail(**params)
    if res.get('code') == 0:
        return res.get('data')


# 根据作业模板ID查询作业模板详情,测试OK
def job_get_cron_list(request):
    client = get_client_by_request(request)
    params = {
        "bk_biz_id": 2,
        # "cron_name": "cron_name",  # 定时作业名称
        # "cron_id": "cron_name",  # 定时任务ID，如果存在则忽略其他筛选条件，只查询这个指定的作业信息
        # "cron_status": "cron_name",  # 定时作业状态：1.已启动、2.已暂停
        # "creator": "cron_name",  # 定时作业创建人帐号
        # "create_time_start": "cron_name",  # 创建起始时间，YYYY-MM-DD格式
        # "create_time_end": "cron_name",  # 创建结束时间，YYYY-MM-DD格式
        # "last_modify_user": "cron_name",  # 作业修改人帐号
        # "last_modify_time_start": "cron_name",  # 最后修改起始时间，YYYY-MM-DD格式
        # "last_modify_time_end": "cron_name",  # 最后修改结束时间，YYYY-MM-DD格式
        # "start": "cron_name",  # 默认0表示从第1条记录开始返回
        # "length": "cron_name",  # 返回记录数量，不传此参数默认返回全部
    }
    res = client.job.get_cron_list(**params)
    if res.get('code') == 0:
        return res.get('data')
    return res["message"]


# 快速分发文件,测试OK
def job_fast_push_file(request):
    client = get_client_by_request(request)
    params = {
        "bk_biz_id": 2,  # 业务ID
        "account": "root",  # 执行帐号名/别名
        "file_target_path": "/tmp",  # 分发文件的目标路径
        "file_source": [
            {
                "files": [
                    "/root/test_push_file.txt"  # 源目标主机的源文件路径
                ],
                "account": "root",
                "ip_list": [
                    {
                        "bk_cloud_id": 0,
                        "ip": "192.168.148.103"  # 源目标主机
                    },
                ],
                # "custom_query_id": [
                #     "3"
                # ]
            }
        ],
        "ip_list": [
            {
                "bk_cloud_id": 0,
                "ip": "192.168.148.104"  # 目标主机
            },
        ],
    }
    res = client.job.fast_push_file(**params)

    if res.get('code') == 0:
        return True


# 快速执行脚本
def job_fast_execute_script(request):
    """
    快速执行脚本
    :param request:
    :return:
    """
    bk_cloud_id = 0
    ip = "192.168.148.103"
    biz_id = 2
    ip_list = [{
        "bk_cloud_id": bk_cloud_id,
        "ip": ip
    }]
    client = get_client_by_request(request)
    content = """
        #!/bin/bash
        cat /proc/loadavg
    """  # 脚本内容
    params = {
        'bk_username': 'admin',
        'bk_biz_id': int(biz_id),
        'script_content': base64.b64encode(content),
        'account': "root",
        'bk_callback_url': "root",
        'script_type': 1,
        'ip_list': ip_list,
    }  # 参数
    resp = client.job.fast_execute_script(**params)

    if resp.get('code') == 0:
        return resp["data"]


# 获取脚本执行状态,判断脚本是否已经执行完成
def job_get_job_instance_status(request):
    global count
    count += 1
    client = get_client_by_request(request)
    # 查询执行状态
    resp = client.job.get_job_instance_status(
        bk_username='admin',
        bk_biz_id=2,
        job_instance_id=3667430
    )
    if resp.get('data', {}).get('is_finished'):
        count = 0
        return True


# 获取脚本执行结果
def job_get_job_instance_log(request):
    client = get_client_by_request(request)
    # 查询日志
    resp = client.job.get_job_instance_log(
        job_instance_id=3667430,
        bk_biz_id=2,
        bk_username='admin'
    )
    ip_logs = resp.get("data")[0].get('step_results')[0].get("ip_logs")
    return ip_logs


# 启动作业
def job_execute_job(request):
    client = get_client_by_request(request)
    params = {
        "bk_biz_id": 2,
        "bk_job_id": 1,
    }
    res = client.job.execute_job(**params)
    if res.get('code') == 0:
        return res.get('data')
    return res["message"]


# 快速执行SQL脚本
def job_fast_execute_sql(request):
    client = get_client_by_request(request)
    params = {
        "bk_biz_id": 2,
        "script_id": 1,
        "script_content": base64.b64encode("show databases"),
        "script_timeout": 1000,
        "db_account_id": 32,
        "ip_list": [
            {
                "bk_cloud_id": 0,
                "ip": "192.168.102.152"
            },
            {
                "bk_cloud_id": 0,
                "ip": "192.168.102.151"
            }
        ]
    }
    res = client.job.fast_execute_sql(**params)
    if res.get('code') == 0:
        return res.get('data')
    return res["message"]


# 查询用户有权限的DB帐号列表
def job_get_own_db_account_list(request):
    client = get_client_by_request(request)
    params = {
        "bk_username": "admin",
        "bk_biz_id": 2,  # 业务ID
    }
    res = client.job.get_own_db_account_list(**params)
    if res.get('code') == 0:
        return res.get('data')


# 更新定时作业状态
def job_update_cron_status(request):
    client = get_client_by_request(request)
    params = {
        "bk_biz_id": 2,
        "cron_status": 1,  # 1.启动、2.暂停
        "cron_id": 2
    }
    res = client.job.update_cron_status(**params)
    if res.get('code') == 0:
        return res.get('data')
    return res["message"]


# 新建或保存定时作业
def job_save_cron(request):
    client = get_client_by_request(request)
    params = {
        'bk_username': 'admin',
        "bk_biz_id": 1,
        "bk_job_id": 100,
        "cron_name": "test",
        "cron_expression": "0 0/5 * * * ?"
    }
    res = client.job.save_cron(**params)
    if res.get('code') == 0:
        return res.get('data')
    return res["message"]


# 更新定时作业状态
def job_change_cron_status(request):
    client = get_client_by_request(request)
    params = {
        "bk_biz_id": 2,
        "cron_status": 1,  # 1.启动、2.暂停
        "cron_id": 1
    }
    res = client.job.update_cron_status(**params)
    if res.get('code') == 0:
        return res.get('data')
    return res["message"]


################### 蓝鲸配置平台 #######################


# 获取所有业务,测试OK
def cc_search_business(fields=[]):
    """
    获取业务列表
    :param request:
    :return:
    """
    client = get_client_by_user("admin")
    params = {'fields': fields}
    res = client.cc.search_business(**params)
    if res.get('code') == 0:
        return res.get('data', {}).get('info', [])


# 根据业务ID查询集群,测试OK
def cc_search_set(request):
    client = get_client_by_request(request)
    params = {
        'bk_biz_id': 2,
        "fields": ["bk_set_id", "bk_set_name"]
    }
    res = client.cc.search_set(**params)
    if res.get('code') == 0:
        return res.get('data', '').get('info', [])


# 根据条件查询主机,测试OK
def cc_search_host(request):
    client = get_client_by_request(request)
    params = {
        "condition": [
            {"bk_obj_id": "set", "fields": [], "condition": []},
            {"bk_obj_id": "host", "fields": [], "condition": []},
            {"bk_obj_id": "module", "fields": [], "condition": []},
            {"bk_obj_id": "biz", "fields": [], "condition": []},
            {"bk_obj_id": "object", "fields": [], "condition": []}
        ]
    }
    res = client.cc.search_host(**params)  # 根据业务ID和集群ID查询主机
    if res.get('code') == 0:
        return res.get('data', '').get('info', [])


# 获取主机详情
def cc_get_host_base_info(request):
    client = get_client_by_request(request)
    params = {"bk_host_id": 224}
    res = client.cc.get_host_base_info(**params)
    if res.get('code') == 0:
        return res.get('data', [])


# 查询业务实例拓扑,测试OK
def cc_search_biz_inst_topo(request, bk_biz_id):
    client = get_client_by_request(request)
    params = {"bk_biz_id": bk_biz_id}
    res = client.cc.search_biz_inst_topo(**params)
    if res.get('code') == 0:
        return res.get('data')


# 查询实例
def cc_search_inst_by_object(request):
    client = get_client_by_request(request)
    params = {
        "bk_supplier_account": "0",
        "bk_obj_id": "biz",
        "page": {
            "start": 0,
            "limit": 50,
            "sort": "bk_inst_id"
        },
        "fields": [],
        "condition": {}
    }
    res = client.cc.search_inst_by_object(**params)
    if res.get('code') == 0:
        return res.get('data')


# 查询模块
def cc_search_module(request):
    client = get_client_by_request(request)
    params = {
        'bk_biz_id': 2,
        'bk_set_id': 2,
        "bk_supplier_account": "0",
        "fields": [],
        "condition": {},
        "page": {
            "start": 0,
            "limit": 10
        }
    }
    res = client.cc.search_module(**params)
    if res.get('code') == 0:
        return res.get('data')


# 创建模块
def cc_create_module(request):
    client = get_client_by_request(request)
    params = {
        "bk_supplier_account": "0",
        "bk_biz_id": 1,
        "bk_set_id": 10,
        "data": {
            "bk_parent_id": 10,
            "bk_module_name": "test"
        }
    }
    res = client.cc.create_module(**params)
    if res.get('code') == 0:
        return res.get('data')
    return res["message"]


# 创建集群
def cc_create_set(request):
    client = get_client_by_request(request)
    params = {
        "bk_supplier_account": "0",
        "bk_biz_id": 2,
        "data": {
            "bk_parent_id": 1,
            "bk_set_name": "test-set",
            "bk_set_desc": "test-set",
            "bk_capacity": 1000,
            "description": "description"
        }
    }
    res = client.cc.create_set(**params)
    if res.get('code') == 0:
        return res.get('data')
    return res["message"]


# 删除业务
def cc_delete_business(request):
    client = get_client_by_request(request)
    params = {
        "bk_supplier_account": "0",
        "bk_biz_id": 2,
    }
    res = client.cc.delete_business(**params)
    if res.get('code') == 0:
        return res.get('data')
    return res["message"]


# 删除主机
def cc_delete_host(request):
    client = get_client_by_request(request)
    params = {
        "bk_supplier_account": "0",
        "bk_host_id": "1,2,3",
    }
    res = client.cc.delete_host(**params)
    if res.get('code') == 0:
        return res.get('data')
    return res["message"]


# 删除模块
def cc_delete_module(request):
    client = get_client_by_request(request)
    params = {
        "bk_supplier_account": "0",
        "bk_biz_id": 1,
        "bk_set_id": 1,
        "bk_module_id": 1
    }
    res = client.cc.delete_module(**params)
    if res.get('code') == 0:
        return res.get('data')
    return res["message"]


# 删除集群
def cc_delete_set(request):
    client = get_client_by_request(request)
    params = {
        "bk_supplier_account": "0",
        "bk_biz_id": 1,
        "bk_set_id": 1,
    }
    res = client.cc.delete_set(**params)
    if res.get('code') == 0:
        return res.get('data')
    return res["message"]


# 修改业务
def cc_update_business(request):
    client = get_client_by_request(request)
    params = {
        'bk_biz_id': 2,
        "data": {
            "bk_biz_name": "cc_app_test",
            "bk_biz_maintainer": "admin",
            "bk_biz_productor": "admin",
            "bk_biz_developer": "admin",
            "bk_biz_tester": "admin",
        }
    }
    res = client.cc.update_business(**params)
    if res.get('code') == 0:
        return res.get('data')
    return res["message"]


# 更新主机属性
def cc_update_host(request):
    client = get_client_by_request(request)
    params = {
        'bk_username': 'admin',
        "bk_host_id": "1,2,3",
        "data": {
            "bk_host_name": "test"
        }
    }
    res = client.cc.update_host(**params)
    if res.get('code') == 0:
        return res.get('data')
    return res["message"]


# 更新模块
def cc_update_module(request):
    client = get_client_by_request(request)
    params = {
        "bk_supplier_account": 0,
        "bk_biz_id": 1,
        "bk_set_id": 1,
        "bk_module_id": 1,
        "data": {
            "bk_module_name": "test"
        }
    }
    res = client.cc.update_module(**params)
    if res.get('code') == 0:
        return res.get('data')
    return res["message"]


# 更新集群
def cc_update_set(request):
    client = get_client_by_request(request)
    params = {
        "bk_supplier_account": "0",
        "bk_biz_id": 1,
        "bk_set_id": 1,
        "data": {
            "bk_set_name": "test"
        }
    }
    res = client.cc.update_set(**params)
    if res.get('code') == 0:
        return res.get('data')
    return res["message"]
