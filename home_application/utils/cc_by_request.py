# coding: utf-8
# @Time: 2019/10/16 10:00
# @Author: renpingsheng

import json
import requests

from config import APP_CODE, SECRET_KEY, BK_URL


headers = {"Content-Type": "application/json; charset=utf-8"}


def cc_create_classification():
    """
    添加模型分类
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/create_classification/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_classification_id": "cs_test",
        "bk_classification_name": "test_name",
        "bk_classification_icon": "icon-cc-business"
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_create_inst():
    """
    创建实例
    实例名,当创建对象为云区域时为bk_cloud_name
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/create_inst/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_obj_id": "example18",
        "bk_inst_name": "example18",
        "bk_supplier_account": "0",
        "bk_biz_id": 0
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_create_module():
    """
    创建模块
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/create_module/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_id": 0,
        "bk_biz_id": 1,
        "bk_set_id": 10,
        "data": {"bk_parent_id": 10, "bk_module_name": "test"}
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_create_object():
    """
    创建模型
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/create_object/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "creator": "admin",
        "bk_classification_id": "cc_test",
        "bk_obj_name": "cc_test_inst",
        "bk_supplier_account": "0",
        "bk_obj_icon": "icon-cc-business",
        "bk_obj_id": "cc_test_inst"
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_create_object_attribute():
    """
    创建模型属性
    bk_property_type
        singlechar,longchar,int,enum,date,time,objuser,singleasst,multiasst,timezone,bool
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/create_object_attribute/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "creator": "user",
        "isreadonly": False,
        "isonly": False,
        "description": "",
        "unit": "",
        "isrequired": False,
        "editable": False,
        "option": "",
        "placeholder": "",
        "bk_property_group": "default",
        "bk_obj_id": "cc_test_inst",
        "bk_supplier_account": "0",
        "bk_property_id": "cc_test",
        "bk_property_name": "cc_test",
        "bk_property_type": "singlechar",
        "bk_asst_obj_id": "singlechar",
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_create_set():
    """
    添加集群
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/create_set/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_id": 0,
        "bk_biz_id": 1,
        "data": {
            "bk_parent_id": 1,
            "bk_set_name": "test-set",
            "bk_set_desc": "test-set",
            "bk_capacity": 1000,
            "description": "description"
        }
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_create_user_group():
    """
    新建用户分组
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/create_user_group/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_account": "cs_test",
        "group_name": "管理员",
        "user_list": "owen;tt"
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_delete_business():
    """
    删除业务
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/delete_business/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_classification_id": "cs_test",
        "bk_supplier_id": 0,
        "bk_biz_id": 1
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_delete_classification():
    """
    删除模型分类
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/delete_classification/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "id": 1,
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_delete_host():
    """
    删除主机
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/delete_host/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_classification_id": "cs_test",
        "bk_supplier_id": 0,
        "bk_host_id": "1,2,3",
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_delete_inst():
    """
    删除对象实例
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/delete_inst/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_account": "cc_test",
        "bk_obj_id": "test_name",
        "bk_inst_id": "icon-cc-business"
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_delete_module():
    """
    删除模块
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/delete_module/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 1,
        "bk_set_id": 1,
        "bk_module_id": 1
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_delete_object():
    """
    删除模型
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/delete_object/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "id": "cs_test",
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_delete_object_attribute():
    """
    添加模型分类
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/delete_object_attribute/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "id": "icon-cc-business"
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_delete_set():
    """
    删除集群
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/delete_set/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 1,
        "bk_set_id": 10
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_delete_user_group():
    """
    删除用户分组
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/delete_user_group/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_account": "cs_test",
        "group_id": "test_name",
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_create_business():
    """
    新建业务
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/create_business/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_id": 0,
        "data": {
            "bk_biz_name": "cc_app_test",
            "bk_biz_maintainer": "admin",
            "bk_biz_productor": "admin",
            "bk_biz_developer": "admin",
            "bk_biz_tester": "admin",
            "time_zone": "Asia/Shanghai"
        }
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_bind_role_privilege():
    """
    绑定角色权限
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/bind_role_privilege/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_account": "0",
        "bk_obj_id": "biz",
        "bk_property_id": "test",
        "data": ["hostupdate", "hosttrans", "topoupdate", "customapi", "proconfig"]
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_add_host_to_resource():
    """
    添加模型分类
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/add_host_to_resource/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": "2",
        "bk_supplier_id": 0,
        "host_info": {
            "0": {
                "bk_host_innerip": "10.0.0.1",
                "bk_cloud_id": 0,
                "import_from": "3"
            }
        }
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_search_group_privilege():
    """
    查询分组权限
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/search_group_privilege/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_account": "icon-cc-business",
        "group_id": "icon-cc-business",
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_search_host():
    """
    根据条件查询主机
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/search_host/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "condition": [
            {
                "bk_obj_id": "host",
                "fields": ["bk_host_name", "bk_host_innerip", "bk_host_id", "bk_cloud_id", ],
            },
            {
                "bk_obj_id": "biz",
                "fields": ["bk_biz_id", "bk_biz_name"],
            }
        ],
        # "page": {"start": 0, "limit": 10}
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_search_inst():
    """
    查询实例
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/search_inst/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_obj_id": "admin",
        "bk_supplier_account": "admin",
        "page": {"start": 0, "limit": 10, "sort": "-bk_inst_id"},
        "fields": {},
        "condition": {}
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_search_inst_association_topo():
    """
    查询实例关联拓扑
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/search_inst_association_topo/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_account": 0,
        "bk_obj_id": 0,
        "bk_inst_id": 0,
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_search_inst_by_object():
    """
    查询给定模型的实例信息
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/search_inst_by_object/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_account": "0",
        "bk_obj_id": "biz",
        "fields": [],
        "condition": {},
        "page": {"start": 0, "limit": 10, "sort": ""}
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_search_module():
    """
    查询模块
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/search_module/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_id": "admin",
        "bk_biz_id": "admin",
        "bk_set_id": "admin",
        "fields": ["bk_module_name"],
        "condition": {"bk_module_name": "test"},
        "page": {"start": 0, "limit": 10}
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_search_objects():
    """
    查询模型
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/search_objects/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "creator": "admin",
        "modifier": "admin",
        "bk_classification_id": "admin",
        "bk_obj_id": "admin",
        "bk_obj_name": "admin",
        "bk_supplier_account": "admin",
        "bk_username": "admin",
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_search_object_attribute():
    """
    查询对象模型属性
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/search_object_attribute/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_obj_id": "process",
        "bk_supplier_account": "0"
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_search_object_topo():
    """
    查询普通模型拓扑
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/search_object_topo/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_classification_id": "cs_test",
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_get_user_privilege():
    """
    查询用户权限
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/get_user_privilege/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_account": 0,
        "user_name": 0,
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_search_biz_inst_topo():
    """
    查询业务实例拓扑
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/search_biz_inst_topo/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_account": "0",
        "bk_biz_id": "biz",
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_search_business(fields=[], condition={}, page={}):
    """
    查询业务
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/search_business/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_id": 0,
        # "fields": ["bk_biz_id", "bk_biz_name"],
        "fields": fields,
        "condition": condition,
        # "condition": {"bk_biz_name": "esb-test"},
        # "page": {"start": 0, "limit": 10, "sort": ""}
        "page": page
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_search_classifications():
    """
    添加模型分类
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/search_classifications/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "creator": "admin",
        "modifier": "admin",
        "bk_classification_id": "admin",
        "bk_obj_id": "admin",
        "bk_obj_name": "admin",
        "bk_supplier_account": "admin",
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_search_object_topo_graphics():
    """
    查询拓扑图
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/search_object_topo_graphics/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_search_set():
    """
    查询集群
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/search_set/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": "admin",
        "bk_supplier_id": "admin",
        "fields": ["bk_set_name"],
        "condition": {"bk_set_name": "test"},
        "page": {"start": 0, "limit": 10, "sort": "bk_set_name"}
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_search_subscription():
    """
    查询订阅
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/search_subscription/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_search_user_group():
    """
    查询用户分组
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/search_user_group/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_account": "0",
        "group_name": "biz",
        "user_list": "test",
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_get_host_base_info():
    """
    获取主机基础信息详情
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/get_host_base_info/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_host_id": "2",
        "bk_supplier_id": 0,
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_get_operation_log():
    """
    批量删除对象实例
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/get_operation_log/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_biz_id": "admin",
        "op_target": "admin",
        "bk_username": "admin",
        "op_type": "admin",
        "condition": {
            "bk_biz_id": 99999,
            "ext_key": {"$in": ["127.0.0.23", "127.0.0.22"]},
            "op_target": "host",
            "op_type": "add",
            "op_time": ["2017-12-25 10:10:10", "2017-12-25 10:10:11"]
        },
        "start": 0,
        "limit": 10,
        "sort": "-create_time"
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_get_role_privilege():
    """
    获取角色绑定权限
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/get_role_privilege/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_account": "cs_test",
        "bk_obj_id": "cs_test",
        "bk_property_id": "cs_test",
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_transfer_resourcehost_to_idlemodule():
    """
    资源池主机分配至业务的空闲机模块
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/transfer_resourcehost_to_idlemodule/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 1,
        "bk_host_id": [9, 10]
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_transfer_host_module():
    """
    业务内主机转移模块
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/transfer_host_module/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 1,
        "bk_host_id": [9, 10],
        "bk_module_id": [10],
        "is_increment": True
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_transfer_host_to_faultmodule():
    """
    上交主机到业务的故障机模块
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/transfer_host_to_faultmodule/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 1,
        "bk_host_id": [9, 10]
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_transfer_host_to_idlemodule():
    """
    上交主机到业务的空闲机模块
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/transfer_host_to_idlemodule/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 1,
        "bk_host_id": [9, 10]
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_transfer_host_to_resourcemodule():
    """
    上交主机至资源池
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/transfer_host_to_resourcemodule/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 1,
        "bk_host_id": [9, 10]
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_update_classification():
    """
    更新模型分类
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/update_classification/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "id": "admin",
        "bk_classification_name": "cc_test_new",
        "bk_classification_icon": "icon-cc-business"
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_update_event_subscribe():
    """
    修改订阅
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/update_event_subscribe/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "subscription_name": "mysubscribe",
        "bk_biz_id": "mysubscribe",
        "bk_supplier_account": "mysubscribe",
        "subscription_id": "mysubscribe",
        "system_name": "SystemName",
        "callback_url": "http://127.0.0.1:8080/callback",
        "confirm_mode": "httpstatus",
        "confirm_pattern": "200",
        "subscription_form": "hostcreate",
        "timeout": 10
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_update_host():
    """
    更新主机属性
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/update_host/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_host_id": "1,2,3",
        "data": {
            "bk_host_name": "test"
        }
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_update_inst():
    """
    更新对象实例
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/update_inst/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_account": "2",
        "bk_obj_id": "2",
        "bk_inst_id": "2",
        "bk_inst_name": "2",
        "bk_cloud_name": 0,
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_update_module():
    """
    更新模块
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/update_module/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 1,
        "bk_set_id": 1,
        "bk_module_id": 1,
        "data": {
            "bk_module_name": "test"
        }
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_update_object():
    """
    更新模型定义
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/update_object/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "modifier": "admin",
        "id": "admin",
        "bk_classification_id": "cc_test",
        "bk_obj_name": "cc2_test_inst",
        "bk_supplier_account": "0",
        "bk_obj_icon": "icon-cc-business",
        "position": "{\"ff\":{\"x\":-863,\"y\":1}}"
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_update_object_attribute():
    """
    更新对象模型属性
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/update_object_attribute/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "description": "",
        "placeholder": "",
        "id": 2,
        "unit": "",
        "isonly": False,
        "isreadonly": False,
        "isrequired": False,
        "bk_property_group": "default",
        "option": "{\"min\":\"1\",\"max\":\"4\"}",
        "bk_property_name": "aaa",
        "bk_property_type": "int",
        "bk_asst_obj_id": ""
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_update_set():
    """
    更新集群
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/update_set/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": 1,
        "bk_set_id": 1,
        "data": {
            "bk_set_name": "test"
        }
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_update_user_group():
    """
    更新用户分组
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/update_user_group/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_account": "mysubscribe",
        "group_id": "mysubscribe",
        "group_name": "mysubscribe",
        "user_list": "owen;tt"
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_update_business_enable_status():
    """
    修改业务启用状态
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/update_business_enable_status/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_biz_id": "3",
        "bk_supplier_account": "0",
        "flag": "enable"
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")


def cc_update_business():
    """
    更新业务信息
    :return:
    """
    url = "{0}/api/c/compapi/v2/cc/update_business/".format(BK_URL)
    kwargs = {
        "bk_app_code": APP_CODE,
        "bk_app_secret": SECRET_KEY,
        "bk_username": "admin",
        "bk_supplier_id": 0,
        "bk_biz_id": 1,
        "data": {
            "bk_biz_name": "cc_app_test",
            "bk_biz_maintainer": "admin",
            "bk_biz_productor": "admin",
            "bk_biz_developer": "admin",
            "bk_biz_tester": "admin",
        }
    }
    response = requests.post(url=url, data=json.dumps(kwargs), verify=False)
    if response.status_code == 200:
        return json.loads(response.content).get("data")
