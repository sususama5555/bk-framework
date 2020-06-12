from django.http import JsonResponse
from home_application.utils.bk_api_by_client import cc_search_business, bk_login_get_all_users


def get_biz_list(request):
    fields = ["bk_biz_id", "bk_biz_name"]
    data = cc_search_business(fields)
    return JsonResponse({"result": True, "data": data})


def get_user_list(request):
    res_data = bk_login_get_all_users(request)
    return JsonResponse({"result": True, "data": res_data})