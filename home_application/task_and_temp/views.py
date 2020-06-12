# coding: utf-8

import json
import os
import time
import datetime
from wsgiref.util import FileWrapper

import xlrd
from django.views.generic import View
from django.utils.encoding import escape_uri_path
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from home_application.task_and_temp.models import JobTemplate, JobToDoList, JobObject
from home_application.utils.parse_time import get_current_timestr


def job_center_html(request):
    return render(request, 'home_application/demo/task_center.html')


def job_temp_html(request):
    return render(request, 'home_application/demo/temp_center.html')


def check_upload_wrapper(func):
    def inner(*args, **kwargs):
        if not os.path.exists("upload/"):
            os.makedirs("upload/")
        return func(*args, **kwargs)

    return inner


class JobTempView(View):
    def get(self, request, *args, **kwargs):
        try:
            job_temp_query = JobTemplate.objects.all()
        except Exception:
            return JsonResponse({"result": False})
        search_biz = request.GET.get("search_biz")
        search_type = request.GET.get("search_type")
        search_name = request.GET.get("search_name")
        if search_biz:
            job_temp_query = job_temp_query.filter(bk_biz_name__contains=search_biz)
        if search_type:
            job_temp_query = job_temp_query.filter(temp_type=search_type)
        if search_name:
            job_temp_query = job_temp_query.filter(temp_name__contains=search_name)
        res_data = [i.to_dict() for i in job_temp_query]
        return JsonResponse({"result": True, "data": res_data})

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        job_temp_obj = {
            "bk_biz_name": data.get("add_form", {}).get("add_biz_name"),
            "temp_name": data.get("add_form", {}).get("add_temp_name"),
            "temp_type": data.get("add_form", {}).get("add_temp_type"),
            "creater": request.user.username,
            "file_path": data.get("file_list")
        }
        try:
            JobTemplate.objects.create(**job_temp_obj)
            return JsonResponse({"result": True})
        except Exception as e:
            print(e)
            return JsonResponse({"result": False})

    def delete(self, request, *args, **kwargs):
        data = json.loads(request.body)
        pk = data.get("pk")
        try:
            JobTemplate.objects.filter(pk=pk).delete()
            return JsonResponse({"result": True})
        except Exception as e:
            print(e)
            return JsonResponse({"result": False})

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        pk = data.get("pk")
        job_temp_obj = {
            "bk_biz_name": data.get("edit_form", {}).get("edit_biz_name"),
            "temp_name": data.get("edit_form", {}).get("edit_temp_name"),
            "temp_type": data.get("edit_form", {}).get("edit_temp_type"),
            "updater": request.user.username,
            "file_path": data.get("file_list"),
            "update_time": datetime.datetime.today()
        }
        try:
            JobTemplate.objects.filter(id=pk).update(**job_temp_obj)
            return JsonResponse({"result": True})
        except Exception as e:
            print(e)
            return JsonResponse({"result": False})


def update_job_status():
    job_obj_query = JobObject.objects.all()
    for job_obj in job_obj_query:
        to_do_query = JobToDoList.objects.filter(job_id=job_obj.pk).values("status")
        status_list = [i.get("status") for i in to_do_query]
        if status_list.count(u"已完成") == len(status_list):
            job_obj.status = u"已完成"
        elif status_list.count(u"已完成") == 0:
            job_obj.status = u"待操作"
        else:
            job_obj.status = u"操作中"
        job_obj.save()


class JobView(View):
    def get(self, request, *args, **kwargs):
        # update_job_status()
        try:
            job_query = JobObject.objects.all()
        except Exception:
            return JsonResponse({"result": False})
        search_biz = request.GET.get("search_biz")
        search_temp_type = request.GET.get("search_temp_type")
        search_status = request.GET.get("search_status")
        search_creater = request.GET.get("search_creater")
        search_name = request.GET.get("search_name")
        search_operate_id = request.GET.get("search_operate_id")
        if search_biz:
            job_query = job_query.filter(bk_biz_name__contains=search_biz)
        if search_temp_type:
            job_query = job_query.filter(job_type=search_temp_type)
        if search_name:
            job_query = job_query.filter(job_name__contains=search_name)
        if search_creater:
            job_query = job_query.filter(creater=search_creater)
        if search_operate_id:
            job_query = job_query.filter(identifi__contains=search_operate_id)
        if search_status:
            job_query = job_query.filter(status=search_status)
        res_data = [i.to_dict() for i in job_query]
        return JsonResponse({"result": True, "data": res_data})

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        temp_id = data.get("add_form", {}).get("add_temp_name").split(":")[0]
        temp_name = data.get("add_form", {}).get("add_temp_name").split(":")[1]
        job_obj = {
            "bk_biz_name": data.get("add_form", {}).get("add_biz_name"),
            "job_name": data.get("add_form", {}).get("add_job_name"),
            "temp_id": temp_id,
            "temp_name": temp_name,
            "job_type": data.get("add_form", {}).get("add_job_type"),
            "creater": request.user.username,
            "identifi": data.get("add_form", {}).get("add_operate_id")
        }
        try:
            job_obj = JobObject.objects.create(**job_obj)
            try:
                job_temp_obj = JobTemplate.objects.get(pk=temp_id)
                file_path = eval(job_temp_obj.file_path)[0].get("url")
                data = read_excel(file_path)
                querysets = []
                for d in data:
                    querysets.append(JobToDoList(
                        temp_id=temp_id,
                        job_id=job_obj.id,
                        operate=d.get("operate"),
                        note=d.get("note"),
                        creater=request.user.username,
                        confirmer=d.get("confirmer")
                    ))
                JobToDoList.objects.bulk_create(querysets)
            except Exception:
                return JsonResponse({"result": False})
            return JsonResponse({"result": True})
        except Exception as e:
            print(e)
            return JsonResponse({"result": False})

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass


@csrf_exempt
@check_upload_wrapper  # 装饰器，检查后台是否有`upload/`目录，如果没有则创建
def upload_job_temp(request):
    file_obj = request.FILES.get('file')  # 获取上传的文件对象
    t = time.strftime('%Y%m%d%H%M%S')
    now_file_name = t + '.' + file_obj.name.split('.')[-1]  # 得到文件在后台的保存名字
    file_path = os.path.join('upload', now_file_name)
    with open(file_path, "wb") as f:
        for line in file_obj.chunks():
            f.write(line)

    return JsonResponse({'result': True, 'data': [{"name": file_obj.name, "url": file_path}]})  # 必须要返回文件保存路径


def download_temp_simple(request):
    file_name = u"checklist.xls"
    file_path = os.path.join("upload/sample_temp", file_name)
    file = open(file_path, 'rb')
    response = HttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = "attachment;filename*=utf-8''{}".format(escape_uri_path(file_name))
    return response


def download_temp_file(request):
    """中文名文件下载(编码问题)"""
    temp_id = request.GET.get("id")
    temp_obj = JobTemplate.objects.get(pk=temp_id)
    file = open(eval(temp_obj.file_path)[0].get("url"), 'rb')
    file_name = eval(temp_obj.file_path)[0].get("name")
    response = HttpResponse(file)
    response["Content-Type"] = "application/octet-stream"
    response["Content-Disposition"] = "attachment;filename*=UTF-8''{}".format(escape_uri_path(file_name))
    return response

    # """英文名文件下载"""
    # temp_id = request.GET.get("id")
    # temp_obj = JobTemplate.objects.get(pk=temp_id)
    # file = open(eval(temp_obj.file_path)[0].get("url"), 'rb')
    # file_name = eval(temp_obj.file_path)[0].get("name")
    # response = HttpResponse(file)
    # response['Content-Type'] = 'application/octet-stream'
    # response['Content-Disposition'] = 'attachment;filename="{}"'.format(file_name)
    # return response


def test(request):
    to_do_count = JobToDoList.objects.count()
    if to_do_count < 10:
        job_obj_query = JobObject.objects.values("")
        for job in job_obj_query:
            obj = JobTemplate.objects.get(id=job.temp_id)
            data = read_excel(obj.file_path)
            for d in data:
                to_do_obj = {
                    "job_id": job.id,
                    "temp_id": job.temp_id,
                    "operate": d.get("operate"),
                    "note": d.get("note"),
                    "creater": d.get("user"),
                }
                JobToDoList.objects.create(**to_do_obj)
    return JsonResponse({"result": True})


def get_job_detail(request):
    job_id = request.GET.get("job_id")
    try:
        to_do_query = JobToDoList.objects.filter(job_id=job_id)
    except Exception:
        return JsonResponse({"result": True})
    res_data = [i.to_dict() for i in to_do_query]
    return JsonResponse({"result": True, "data": res_data})


def confirm_operate(request):
    data = json.loads(request.body)
    id = data.get("id")
    try:
        JobToDoList.objects.filter(id=id).update(
            status=u"已完成",
            confirmer=request.user.username,
            answer_time=datetime.datetime.now()
        )
        return JsonResponse({"result": True, "data": {
            "confirmer": request.user.username,
            "answer_time": get_current_timestr(),
        }})
    except Exception as e:
        print(e)
        return JsonResponse({"result": False})


# 读取Excel文件
def read_excel(file_name):
    # 路径前加 r，读取的文件路径
    # 文件路径的中文转码
    file_path = file_name.encode('gbk').decode('utf-8')

    # 获取数据
    data = xlrd.open_workbook(file_path)

    # 获取sheet，通常为 Sheet1
    table = data.sheet_by_name(u'Sheet1')

    res_data = []

    # 获取excel文件的总行数
    nrows = table.nrows
    ncols = table.ncols

    # 从第二行开始读取数据
    for i in range(1, nrows):
        # 读取每一行第一列的数据
        step = table.cell(i, 0).value
        operate = table.cell(i, 1).value
        note = table.cell(i, 2).value
        user = table.cell(i, 3).value
        res_data.append({
            "step": step,
            "operate": operate,
            "note": note,
            "user": user,
        })
    return res_data
