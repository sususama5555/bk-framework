# -*- coding: utf-8 -*-
from config import RUN_VER
if RUN_VER == 'open':
    from blueapps.patch.settings_open_saas import *  # noqa
else:
    from blueapps.patch.settings_paas_services import  * # noqa

# 预发布环境
RUN_MODE = 'STAGING'

# 正式环境的日志级别可以在这里配置
# V2
# import logging
# logging.getLogger('root').setLevel('INFO')
# V3
# import logging
# logging.getLogger('app').setLevel('INFO')


# 预发布环境数据库可以在这里配置

# DATABASES.update(
#     {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': APP_ID,  # 数据库名
#             'USER': 'root',  # 数据库用户
#             'PASSWORD': '0N9LZr3ksu',  # 数据库密码
#             'HOST': '192.168.163.5',  # 数据库主机
#             'PORT': '3306',  # 数据库端口
#         },
#     }
# )
DATABASES.update(
    {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': APP_ID,  # 数据库名
            'USER': 'bkds',  # 数据库用户
            'PASSWORD': 'bkds_test',  # 数据库密码
            'HOST': '47.112.240.167',  # 数据库主机
            'PORT': '3306',  # 数据库端口
        },
    }
)


