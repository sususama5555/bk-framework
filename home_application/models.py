# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
from home_application.utils.parse_time import parse_datetime_to_timestr
from .host_and_monitor.models import HostInfo

class FileInfo(models.Model):
    """备份文件信息"""
    ip = models.CharField(max_length=64, default="")
    path = models.CharField(max_length=128, default="")
    number = models.IntegerField(blank=True, null=True)
    file_list = models.CharField(max_length=128, default="")
    size = models.CharField(max_length=128, default="")
    done = models.BooleanField(default=False)
    creater = models.CharField(max_length=128, default="")
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def to_dict(self):
        return {
            "ip": self.ip,
            "file_list": self.file_list,
            "number": self.number,
            "size": self.size,
            "creater": self.creater,
            "create_time": parse_datetime_to_timestr(self.create_time),
        }


class Template(models.Model):
    """模板信息"""
    business = models.CharField(max_length=64, default="")
    type = models.CharField(max_length=64, default="")
    name = models.CharField(max_length=64, default="")
    creator = models.CharField(max_length=64, default="")
    updator = models.CharField(max_length=64, default="")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Task(models.Model):
    """任务信息"""
    name = models.CharField(max_length=64, default="")
    type = models.CharField(max_length=64, default="")
    template = models.CharField(max_length=64, default="")
    symbol = models.CharField(max_length=64, default="")
    business = models.CharField(max_length=64, default="")
    creator = models.CharField(max_length=64, default="")
    create_at = models.DateTimeField(auto_now_add=True)