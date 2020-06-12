# coding: utf-8
# Datetime:  17:09
# Author: renpingsheng


import time
import datetime


def get_range_date_list(interval_days):
    res_data = []
    for i in range(interval_days, 1, -1):
        tmp = datetime.date.today() - datetime.timedelta(days=i)
        res_data.append(parse_datetime_to_timestr(tmp, flag=False))
    return res_data


def get_current_timestr(flag=1):
    """
    获取当前时间字符串
    :param flag: 根据flag的值判断输出时间字符串的格式
    :return: 时间字符串
    """
    if flag == 1:
        c_timestr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 2019-01-01 12:12:12
    elif flag == 2:
        c_timestr = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))  # 2019-01-01 12:12
    else:
        c_timestr = time.strftime('%Y-%m-%d', time.localtime(time.time()))  # 2019-01-01
    return c_timestr


def parse_timestr_to_timestamp(time_str, flag=1):
    """
    把时间字符串转换为时间戳格式
    :param time_str: 时间字符串,格式为：2019-01-01 12:12:12 或 2019-01-01
    :param flag: 标志位，决定输入时间字符串的格式
    :return: 时间戳格式
    """
    struct_time = 0
    if flag == 1:
        struct_time = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")  # 2019-01-01 12:12:12
    elif flag == 2:
        struct_time = time.strptime(time_str, "%Y-%m-%d")  # 2019-01-01
    elif flag == 3:
        struct_time = time.strptime(time_str, "%Y-%m-%d %H:%M")  # 2019-01-01 12:12
    elif flag == 4:
        struct_time = time.strptime(time_str, "%Y-%m")  # 2019-01
    return time.mktime(struct_time)


def parse_timestamp_to_timestr(time_stamp, flag=True):
    """
    把时间戳转换为时间字符串
    :param time_stamp: 时间戳
    :param flag: 标志位，可以指定输出时间字符串的格式
    :return: 时间字符串,格式为：2019-01-01 12:12:12 或 2019-01-01
    """
    localtime = time.localtime(time_stamp)
    if flag:
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
    else:
        time_str = time.strftime("%Y-%m-%d", localtime)
    return time_str


def is_workday(time_str):
    """
    传入时间字符串，判断传入时间字符串是否是工作日
    :param time_str: 必须是时间字符串类型，比如："2019-01-21 14:30:31"
    :return: True/False，是否为非工作日
    """
    tmp = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    workday_list = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    holiday_list = ["Sat", "Sun"]

    week = time.strftime("%a", tmp)
    if week in workday_list:
        return True
    else:
        return False


def is_holiday(time_str):
    """
    传入时间字符串，判断传入时间字符串是否是工作日
    :param time_str: 必须是时间字符串类型，比如："2019-01-21 14:30:31"
    :return: True/False，是否为非工作日
    """
    tmp = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    workday_list = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    holiday_list = ["Sat", "Sun"]

    week = time.strftime("%a", tmp)
    if week in holiday_list:
        return True
    else:
        return False


def covert_time(time_str):
    """
    把时间段转换为秒数
    :param time_str:
    :return:
    """
    if time_str.endswith("h"):
        stamp = float(time_str.strip("h")) * 3600
    elif time_str.endswith("m"):
        stamp = float(time_str.strip("m")) * 60
    else:
        stamp = float(time_str)
    return stamp


################################################

def parse_format_timestr(format_timestr):
    """
    将格式字符串转换为时间戳
    :param format_timestr: 格式字符串,格式： "Sat Mar 28 22:24:24 2016"
    :return:
    """
    tmp_timestamp = time.mktime(time.strptime(format_timestr, "%a %b %d %H:%M:%S %Y"))
    return tmp_timestamp


def parse_datetime_to_timestr(datetime_str, flag=True):
    """
    把datetime时间转化成时间字符串
    :param datetime_str: datetime生成的时间，例子：datetime.datetime.now()
    或者： datetime.datetime.now() - datetime.timedelta(hours=1)       # 一个小时之前
    或者： datetime.datetime.now() - datetime.timedelta(days=1)        # 一天之前
    :return:
    """
    # 将日期转化为字符串 datetime => string
    # 在数据库中定义字段信息时为：models.DateTimeField(auto_now_add=True)
    # 查询数据库之后，使用此方法把查询到的时间转换成可用的时间字符串
    # when_insert__range=(an_hour_time, now_time)
    # an_hour_time和 now_time 都是 datetime时间字符串，查询两个datetime时间字符串之间的数据
    if flag:
        return datetime_str.strftime('%Y-%m-%d %H:%M:%S')
    return datetime_str.strftime('%Y-%m-%d')


def parse_timestr_to_datetime(time_str, flag=True):
    """
    把时间字符串转化成datetime
    :param time_str: 时间字符串，比如：2019-06-25  00:00
    :return: datetimeu时间
    """
    if flag:
        time_str = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    else:
        time_str = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M")
    return time_str


def parse_datetime_to_timestamp(datetime_str):
    """
    把datetime时间转化为时间戳
    :param datetime_str: datetime生成的时间，例子：datetime.datetime.now()
    或者： datetime.datetime.now() - datetime.timedelta(hours=1)       # 一个小时之前
    或者： datetime.datetime.now() - datetime.timedelta(days=1)        # 一天之前
    :return: 时间戳，比如：1561561837.0
    """
    tmp_time_stamp = time.mktime(datetime_str.timetuple())
    return tmp_time_stamp


def parse_timestamp_to_datetime(timestamp):
    """
    把datetime时间转化为时间戳
    :param datetime_str: datetime生成的时间，例子：datetime.datetime.now()
    或者： datetime.datetime.now() - datetime.timedelta(hours=1)       # 一个小时之前
    或者： datetime.datetime.now() - datetime.timedelta(days=1)        # 一天之前
    :return: 时间戳，比如：1561561837.0
    """
    tmp_datetime = datetime.datetime.fromtimestamp(timestamp)
    return tmp_datetime













