from django.http import JsonResponse
from home_application.utils.bk_api_by_client import cc_search_business, bk_login_get_all_users
from blueking.component.shortcuts import get_client_by_request, get_client_by_user


def get_biz_list(request):
    fields = ["bk_biz_id", "bk_biz_name"]
    data = cc_search_business(request, fields)
    return JsonResponse({"result": True, "data": data})


def get_user_list(request):
    res_data = bk_login_get_all_users(request)
    return JsonResponse({"result": True, "data": res_data})


def search_biz(request):
    # 查询业务
    biz_list = []
    # client = get_client_by_user('admin')
    client = get_client_by_request(request)
    biz_result = client.cc.search_business()
    for biz in biz_result["data"]["info"]:
        biz_list.append({"id": biz["bk_biz_id"], "name": biz["bk_biz_name"]})

    return JsonResponse({"result": True, "data": biz_list})
