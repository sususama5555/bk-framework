# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
from home_application.utils.parse_time import parse_datetime_to_timestr


class BackupLog(models.Model):
    """备份文件信息"""
    ip = models.CharField(max_length=64, default="")
    path = models.CharField(max_length=128, default="")
    number = models.IntegerField(blank=True, null=True)
    file_list = models.CharField(max_length=128, default="")
    size = models.CharField(max_length=128, default="")
    job_instance_id = models.IntegerField(blank=True, null=True)
    job_link = models.CharField(max_length=128, default="")
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
            "job_link": self.job_link,
        }
