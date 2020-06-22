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

from blueking.component.shortcuts import get_client_by_user, get_client_by_request
# 跨域！
from django.views.decorators.csrf import csrf_exempt
# from django.template import Context, Template

from .host_and_monitor.models import HostInfo
# from .models import Template
# from .models import Task
# from .models import BackupLog


# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
# 页面跳转


def home(request):
    """
    首页
    """
    return render(request, 'home_application/index_home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render(request, 'home_application/dev_guide.html')


def contact(request):
    """
    联系页
    """
    return render(request, 'home_application/contact.html')


def report_link(request):
    id = request.GET.get("id")
    return render(request, 'home_application/program/report.html', {"id": id})
