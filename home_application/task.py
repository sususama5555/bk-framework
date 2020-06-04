# -*- coding: utf-8 -*-
import json
import datetime
import base64
from celery.task import task, periodic_task
from .models import HostInfo

from blueking.component.shortcuts import get_client_by_user


# @periodic_task()
def get_loadreport():
    client = get_client_by_user('admin')
    script = "cat /proc/loadavg"
    params = {
        "bk_biz_id": 2,
        "script_content": str(base64.b64encode(script.encode("utf-8"))),
        "account": "root",
        "ip_list": [
            {
                "bk_cloud_id": 0,
                "ip": "192.168.102.208"
            }
        ]
    }
    data = client.job.fast_execute_script(**params)
    return data


# @periodic_task(run_every=datetime.timedelta(seconds=1))
def polling_job():
    pass