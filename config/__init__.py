# -*- coding: utf-8 -*-
from __future__ import absolute_import

__all__ = ['celery_app', 'RUN_VER', 'APP_CODE', 'SECRET_KEY', 'BK_URL', 'BASE_DIR']

import os

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from blueapps.core.celery import celery_app

# app 基本信息


def get_env_or_raise(key):
    """Get an environment variable, if it does not exist, raise an exception
    """
    value = os.environ.get(key)
    if not value:
        raise RuntimeError(
            ('Environment variable "{}" not found, you must set this variable to run this application.'
             ' See http://docs.open.oa.com/topics/faq_for_developing#36-本地开发时报错-environment-variable-x-not-found-怎么办'
             ).format(key)
        )
    return value


# 这些变量将由平台通过环境变量提供给应用，本地开发时需手动配置，详见：http://docs.open.oa.com/topics/company_tencent/python_framework_usage#29-配置环境变量
# 应用 ID
# APP_CODE = 'spr-practice-v1'
# # 应用用于调用云 API 的 Secret
# SECRET_KEY = '066d5f95-b630-4449-ae67-22c9524efcbe'
APP_CODE = 'spr-exam'
# 应用用于调用云 API 的 Secret
SECRET_KEY = '88815d10-f829-4b41-a5a2-1fb035a3634b'

# SaaS运行版本，如非必要请勿修改
RUN_VER = 'open'
# 蓝鲸SaaS平台URL，例如 http://paas.bking.com
BK_URL = 'http://paas.dev.com'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(
    __file__)))
