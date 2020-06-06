# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class HostInfo(models.Model):
    """主机信息"""
    ip = models.CharField(max_length=64, default="")
    name = models.CharField(max_length=64, default="")
    business = models.CharField(max_length=64, default="")
    cloud_area = models.CharField(max_length=64, default="")
    os = models.CharField(max_length=64, default="")


class FileInfo(models.Model):
    """备份文件信息"""
    ip = models.CharField(max_length=64, default="")
    path = models.CharField(max_length=128, default="")
    number = models.IntegerField(max_length=32)
    file_list = models.CharField(max_length=128, default="")
    size = models.IntegerField(max_length=64)
    done = models.BooleanField(default=False)


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
    """模板信息"""
    name = models.CharField(max_length=64, default="")
    type = models.CharField(max_length=64, default="")
    template = models.CharField(max_length=64, default="")
    symbol = models.CharField(max_length=64, default="")
    business = models.CharField(max_length=64, default="")
    creator = models.CharField(max_length=64, default="")
    create_at = models.DateTimeField(auto_now_add=True)