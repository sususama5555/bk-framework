# coding: utf-8

from django.db import models

from django.utils.functional import cached_property
from home_application.utils.parse_time import parse_datetime_to_timestr


class JobTemplate(models.Model):
    bk_biz_name = models.CharField(u"业务名称", max_length=32, blank=True, null=True)
    temp_name = models.CharField(u"模板名称", max_length=32, blank=True, null=True)
    temp_type = models.TextField(u"模板类型", max_length=2048, blank=True, null=True)
    creater = models.CharField(u"创建者", max_length=32, blank=True, null=True)
    updater = models.CharField(u"更新者", max_length=256, blank=True, null=True)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_time = models.DateTimeField(u"更新时间", auto_now_add=True)
    file_path = models.CharField(u"文件保存路径", max_length=256, blank=True, null=True)

    def to_dict(self):
        return {
            "pk": self.pk,
            "bk_biz_name": self.bk_biz_name,
            "temp_name": self.temp_name,
            "temp_type": self.temp_type,
            "creater": self.creater,
            "file_path": self.file_path,
            "updater": self.updater,
            "create_time": parse_datetime_to_timestr(self.create_time),
            "update_time": parse_datetime_to_timestr(self.update_time),
            "file_list": eval(self.file_path),
        }


class TempToDoList(models.Model):
    temp_id = models.IntegerField(u"所属模板", blank=True, null=True)
    operate = models.CharField(u"操作事项", max_length=256, blank=True, null=True)
    note = models.CharField(u"备注", max_length=256, blank=True, null=True)
    answer_time = models.DateTimeField(u"完成时间", auto_created=True)
    creater = models.CharField(u"责任人", max_length=256, blank=True, null=True)
    confirmer = models.CharField(u"确认人", max_length=128, blank=True, null=True)

    def to_dict(self):
        return {
            "temp_id": self.temp_id,
            "operate": self.operate,
            "note": self.note,
            "answer_time": self.answer_time,
            "creater": self.creater,
            "confirmer": self.confirmer,
            "pk": self.pk,
        }


class JobObject(models.Model):
    bk_biz_name = models.CharField(u"业务名称", max_length=32, blank=True, null=True)
    job_name = models.CharField(u"任务名称", max_length=16, blank=True, null=True)
    temp_id = models.CharField(u"模板ID", max_length=8, blank=True, null=True)
    temp_name = models.CharField(u"模板名称", max_length=32, blank=True, null=True)
    identifi = models.CharField(u"操作识别号", max_length=256, blank=True, null=True)
    job_type = models.CharField(u"模板类型", max_length=32, blank=True, null=True)
    creater = models.CharField(u"创建者", max_length=32, blank=True, null=True)
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    status = models.CharField(u"状态", max_length=32, default=u"待操作")

    def to_dict(self):
        return {
            "pk": self.pk,
            "bk_biz_name": self.bk_biz_name,
            "job_name": self.job_name,
            "temp_id": self.temp_id,
            "temp_name": self.temp_name,
            "identifi": self.identifi,
            "job_type": self.job_type,
            "creater": self.creater,
            "create_time": parse_datetime_to_timestr(self.create_time),
            "status": self.get_status(),
        }

    def get_status(self):
        job_to_do_query = JobToDoList.objects.filter(job_id=self.pk).values("status")
        status_list = [i.get("status") for i in job_to_do_query]
        if status_list.count(u"已完成") == len(status_list):
            return u"已完成"
        elif status_list.count(u"已完成") == 0:
            return u"待操作"
        else:
            return u"操作中"


class JobToDoList(models.Model):
    job_id = models.IntegerField(u"所属作业", blank=True, null=True)
    temp_id = models.IntegerField(u"所属模板", blank=True, null=True)
    operate = models.CharField(u"操作事项", max_length=256, blank=True, null=True)
    note = models.CharField(u"备注", max_length=256, blank=True, null=True)
    answer_time = models.DateTimeField(u"完成时间", auto_now=True)
    creater = models.CharField(u"责任人", max_length=256, blank=True, null=True)
    confirmer = models.CharField(u"确认人", max_length=128, blank=True, null=True)
    status = models.CharField(u"状态", max_length=16, default=u"未完成")

    def to_dict(self):
        return {
            "temp_id": self.temp_id,
            "operate": self.operate,
            "note": self.note,
            "answer_time": parse_datetime_to_timestr(self.answer_time),
            "creater": self.creater,
            "confirmer": self.confirmer,
            "status": self.status,
            "pk": self.pk,
        }
