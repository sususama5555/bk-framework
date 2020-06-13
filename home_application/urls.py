# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views
from .common import views as common_views
from .task_and_temp import views as task_and_temp_views
from .host_and_monitor import views as host_and_monitor_views

urlpatterns = (
    url(r'^host/$', views.host_list),
    # url(r'^report/$', views.report),
    url(r'^backup/$', views.backup),
    url(r'^backup_log/$', views.backup_log),
    url(r'^dev-guide/$', views.dev_guide),
    url(r'^contact/$', views.contact),
    # url(r'^api/test/$', views.test),
    url(r'^connect_bak/$', views.connect_bak),
    # 页面跳转
    url(r'^report_link/$', views.report_link),
    # 业务urls
    url(r'^get_biz_topo/$', views.get_biz_topo),
    url(r'^get_topo_host/$', views.get_topo_host),
    # url(r'^search_biz/$', views.search_biz),
    # url(r'^search_host/$', views.search_host),
    # url(r'^add_host/$', views.add_host),
    url(r'^init_host_table/$', views.init_host_table),
    # url(r'^delete_host/$', views.delete_host),
    url(r'^detail_report/$', views.detail_report),
    url(r'^search_file/$', views.search_file),
    url(r'^back_up/$', views.back_up),
    url(r'^get_backup_log_table/$', views.get_backup_log_table),
    # 模拟题接口6.6
    # url(r'^$', views.task),
    url(r'^template/$', views.template),
    # url(r'^api/test/$', views.api_test),
    url(r'^init_template/$', views.init_template),
    url(r'^add_template/$', views.add_template),
    url(r'^init_table/$', views.init_table),
    url(r'^delete_template/$', views.delete_template),
    url(r'^edit_template/$', views.edit_template),
    url(r'^search_template/$', views.search_template),
    url(r'^add_task/$', views.add_task),
    url(r'^init_task/$', views.init_task),
    url(r'^upload_template/$', views.upload_template),
    url(r'^download_template/$', views.download_template),

    # =============demo================================
    # common

    url(r'^get_biz_list/$', common_views.get_biz_list),
    url(r'^get_user_list/$', common_views.get_user_list),

    # task_and_template
    url(r'^job_center_html$', task_and_temp_views.job_center_html),
    url(r'^task_center/$', task_and_temp_views.job_center_html),
    url(r'^temp_center/$', task_and_temp_views.job_temp_html),
    url(r'^job_temp_view/$', task_and_temp_views.JobTempView.as_view()),
    url(r'^job_obj_view/$', task_and_temp_views.JobView.as_view()),
    url(r'^upload_job_temp/$', task_and_temp_views.upload_job_temp),
    url(r'^job_temp_test/$', task_and_temp_views.test),
    url(r'^confirm_operate/$', task_and_temp_views.confirm_operate),
    url(r'^get_job_detail/$', task_and_temp_views.get_job_detail),
    url(r'^download_temp_simple/$', task_and_temp_views.download_temp_simple),
    url(r'^download_temp_file/$', task_and_temp_views.download_temp_file),

    # 0613 主机与性能
    url(r'^$', host_and_monitor_views.host_list),
    url(r'^report/$', host_and_monitor_views.report),

    url(r'^api/test/$', host_and_monitor_views.api_test),
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

)
