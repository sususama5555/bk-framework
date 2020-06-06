# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = (
    # url(r'^$', views.home),
    # url(r'^report/$', views.report),
    # url(r'^topo/$', views.topo),
    url(r'^dev-guide/$', views.dev_guide),
    url(r'^contact/$', views.contact),
    # url(r'^api/test/$', views.test),
    url(r'^connect_bak/$', views.connect_bak),
    url(r'^esb_search_biz/$', views.esb_search_biz),
    # 页面跳转
    url(r'^report_link/$', views.report_link),
    # 业务urls
    url(r'^get_biz_topo/$', views.get_biz_topo),
    url(r'^get_topo_host/$', views.get_topo_host),
    url(r'^search_biz/$', views.search_biz),
    url(r'^search_host/$', views.search_host),
    url(r'^add_host/$', views.add_host),
    # url(r'^init_table/$', views.init_table),
    url(r'^delete_host/$', views.delete_host),
    url(r'^detail_report/$', views.detail_report),
    url(r'^search_file/$', views.search_file),
    url(r'^back_up/$', views.back_up),
    # 模拟题接口6.6
    url(r'^$', views.task),
    url(r'^template/$', views.template),
    url(r'^api/test/$', views.api_test),
    url(r'^init_template/$', views.init_template),
    url(r'^add_template/$', views.add_template),
    url(r'^init_table/$', views.init_table),
    url(r'^delete_template/$', views.delete_template),
    url(r'^edit_template/$', views.edit_template),
    url(r'^search_template/$', views.search_template),
    url(r'^add_task/$', views.add_task),
    url(r'^init_task/$', views.init_task),

)
