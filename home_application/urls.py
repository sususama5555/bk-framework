# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views
from .common import views as common_views
from .task_and_temp import views as task_and_temp_views
from .host_and_monitor import views as host_and_monitor_views
from .backup_and_log import views as backup_and_log_views

urlpatterns = (
    # 页面跳转
    # 主机性能与监控
    url(r'^$', host_and_monitor_views.host_list),
    url(r'^report/$', host_and_monitor_views.report),

    # 文件备份与记录
    url(r'^backup/$', backup_and_log_views.backup),
    url(r'^backup_log/$', backup_and_log_views.backup_log),

    # 模板与任务
    url(r'^task_center/$', task_and_temp_views.job_center_html),
    url(r'^temp_center/$', task_and_temp_views.job_temp_html),

    # api test
    url(r'^api/test/$', host_and_monitor_views.api_test),

    # 引导页
    url(r'^home/$', views.home),
    url(r'^dev-guide/$', views.dev_guide),
    url(r'^contact/$', views.contact),
    url(r'^report_link/$', views.report_link),

    # ==========================业务urls================================

    # 公共接口
    url(r'^get_biz_list/$', common_views.get_biz_list),
    url(r'^get_user_list/$', common_views.get_user_list),
    url(r'^search_biz/$', common_views.search_biz),

    # 模板与任务
    url(r'^job_temp_view/$', task_and_temp_views.JobTempView.as_view()),
    url(r'^job_obj_view/$', task_and_temp_views.JobView.as_view()),
    url(r'^upload_job_temp/$', task_and_temp_views.upload_job_temp),
    url(r'^job_temp_test/$', task_and_temp_views.test),
    url(r'^confirm_operate/$', task_and_temp_views.confirm_operate),
    url(r'^get_job_detail/$', task_and_temp_views.get_job_detail),
    url(r'^download_temp_simple/$', task_and_temp_views.download_temp_simple),
    url(r'^download_temp_file/$', task_and_temp_views.download_temp_file),

    # 主机性能与监控
    url(r'^search_biz/$', host_and_monitor_views.search_biz),
    url(r'^search_set/$', host_and_monitor_views.search_set),
    url(r'^search_host/$', host_and_monitor_views.search_host),
    url(r'^add_host/$', host_and_monitor_views.add_host),
    url(r'^get_search_host/$', host_and_monitor_views.get_search_host),
    url(r'^delete_host/$', host_and_monitor_views.delete_host),
    url(r'^get_host_monitor/$', host_and_monitor_views.get_host_monitor),
    url(r'^add_host_monitor/$', host_and_monitor_views.add_host_monitor),
    url(r'^delete_host_monitor/$', host_and_monitor_views.delete_host_monitor),
    url(r'^get_host_list/$', host_and_monitor_views.get_host_list),
    url(r'^get_host_monitor_info/$', host_and_monitor_views.get_host_monitor_info),

    # 文件备份与记录
    url(r'^get_biz_topo/$', backup_and_log_views.get_biz_topo),
    url(r'^get_topo_host/$', backup_and_log_views.get_topo_host),
    url(r'^get_checked_topo_host/$', backup_and_log_views.get_checked_topo_host),
    url(r'^search_biz/$', backup_and_log_views.search_biz),
    url(r'^search_file/$', backup_and_log_views.search_file),
    url(r'^back_up/$', backup_and_log_views.back_up),
    url(r'^get_backup_log_table/$', backup_and_log_views.get_backup_log_table),

)
