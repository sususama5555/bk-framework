# coding: utf-8

from django.db import models

from django.utils.functional import cached_property
from home_application.utils.parse_time import parse_datetime_to_timestr


class HostInfo(models.Model):
    """主机信息"""
    ip = models.CharField(max_length=64, default="")
    name = models.CharField(max_length=64, default="")
    set = models.CharField(max_length=64, default="")
    business = models.CharField(max_length=64, default="")
    cloud_area = models.CharField(max_length=64, default="")
    os = models.CharField(max_length=64, default="")
    # 主机性能
    cpu = models.CharField(max_length=64, default="")
    disk = models.CharField(max_length=64, default="")
    mem = models.CharField(max_length=64, default="")
    is_monitor = models.CharField(max_length=64, default="未监控")

    def to_dict(self):
        return {
            "id": self.id,
            "ip": self.ip,
            "name": self.name,
            "set": self.set,
            "business": self.business,
            "cloud_area": self.cloud_area,
            "os": self.os,
            "cpu": self.cpu,
            "disk": self.disk,
            "mem": self.mem,
            "is_monitor": self.is_monitor,
        }


class hostMonitor(models.Model):
    ip = models.CharField(max_length=64, default="")
    # 主机性能
    cpu = models.CharField(max_length=64, default="")
    disk = models.CharField(max_length=64, default="")
    mem = models.CharField(max_length=64, default="")
    monitor_time = models.DateTimeField(auto_now_add=True)