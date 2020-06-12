# coding: utf-8
# @Time: 2019/10/16 10:01
# @Author: renpingsheng

import base64
import time

from config import APP_CODE, SECRET_KEY, BK_URL

from blueking.component.shortcuts import get_client_by_user, get_client_by_request

count = 0


class FastJobApi(object):
    def __init__(self, bk_biz_id, bk_cloud_id, ip_list, script_content):
        self.client = get_client_by_user('admin')
        self.username = "admin"
        self.biz_id = bk_biz_id
        self.script_content = script_content
        self.ip_list = [{"bk_cloud_id": bk_cloud_id, "ip": i} for i in ip_list.split(",")]

    def _fast_execute_script(self, execute_account="root", param_content='', script_timeout=1000):
        """
        快速执行脚本
        :param execute_account: 执行脚本的账户名
        :param param_content: 执行脚本的参数
        :param script_timeout: 脚本执行超时时间
        :return: job_instance_id
        """
        kwargs = {
            "bk_app_code": APP_CODE,
            "bk_app_secret": SECRET_KEY,
            "bk_biz_id": self.biz_id,
            "bk_username": self.username,
            "script_content": base64.b64encode(self.script_content),
            "ip_list": self.ip_list,
            "script_type": 1,
            "account": execute_account,
            "script_param": base64.b64encode(param_content),
            "script_timeout": script_timeout
        }
        result = self.client.job.fast_execute_script(kwargs)
        if result["result"]:
            return result.get("data", {}).get("job_instance_id")
        return False

    def _get_job_instance_status(self, task_id):
        """
        获取脚本执行状态
        :param task_id: 执行脚本的 job_instance_id
        :return:
        """
        global count
        count += 1
        # 查询执行状态
        resp = self.client.job.get_job_instance_status(
            bk_username=self.username,
            bk_biz_id=self.biz_id,
            job_instance_id=task_id
        )
        if resp.get('data').get('is_finished') or resp.get("is_finished"):
            count = 0
            return True
        elif not resp.get('data').get('is_finished') and count <= 10:
            time.sleep(2)
            return self._get_job_instance_status(task_id)
        else:
            count = 0
            return False

    def _get_job_instance_log(self, task_id):
        """
        查询作业日志
        :param task_id: 执行脚本的 job_instance_id
        :return:
        """
        if self._get_job_instance_status(task_id):
            resp = self.client.job.get_job_instance_log(
                job_instance_id=task_id,
                bk_biz_id=self.biz_id,
                bk_username='admin'
            )
            # print(resp)
            return resp['data'][0]['step_results'][0]['ip_logs']

    def execute_script_and_return(self):
        """
        执行脚本并获取脚本执行结果
        :return: 脚本执行结果
        """
        job_instance_id = self._fast_execute_script()
        if job_instance_id:
            ip_logs = self._get_job_instance_log(job_instance_id)
            return ip_logs


class JobApi(object):
    def __init__(self, bk_biz_id, bk_cloud_id, ip, bk_job_id):
        self.client = get_client_by_user('admin')
        self.username = "admin"
        self.biz_id = bk_biz_id
        # self.bk_callback_url = bk_callback_url
        self.bk_cloud_id = bk_cloud_id
        self.bk_job_id = bk_job_id
        self.ip = ip

    def _get_job_list(self):
        """
        获取所有job列表
        :return:
        """
        params = {
            'bk_username': self.username,
            "bk_biz_id": self.biz_id,
        }
        res = self.client.job.get_job_list(**params)

        if res.get('code') == 0:
            data = res.get('data')
            # for item in data:
            #     bk_biz_id = item.get("bk_biz_id")
            #     tag_id = item.get("tag_id")
            #     name = item.get("name")
            #     bk_job_id = item.get("bk_job_id")
            #     creator = item.get("creator")
            #     step_num = item.get("step_num")
            return data

    def _get_job_detail(self):
        """
        获取指定id的job的详细信息
        :return:
        """
        params = {
            'bk_username': 'admin',
            "bk_biz_id": self.biz_id,
            "bk_job_id": self.bk_job_id,
        }
        res = self.client.job.get_job_detail(**params)

        if res.get('code') == 0:
            data = res.get('data', {})
            return data

    def _get_job_steps(self):
        """
        获取指定id的job的steps
        :return:
        """
        data = self._get_job_detail()
        if data:
            steps = data.get("steps", {})
            account = steps[0].get("account")
            # creator = steps[0].get("creator")
            step_id = steps[0].get("step_id")
            return [{
                "account": account,
                # "creator": creator,
                # "script_content": base64.b64encode("#!/bin/bash\n\nhostname\n"),
                "ip_list": [{
                    "bk_cloud_id": self.bk_cloud_id,
                    "ip": self.ip
                }],
                "step_id": step_id,
                # "script_id": 1052,
                # "script_param": "",
                "script_type": 1
            }]

    def _get_job_instance_status(self, task_id):
        """
        传入job_instance_id，获取job作业结果
        :param task_id: job_instance_id
        :return:
        """
        global count
        count += 1
        # 查询执行状态
        resp = self.client.job.get_job_instance_status(
            bk_username=self.username,
            bk_biz_id=self.biz_id,
            job_instance_id=task_id
        )
        if resp.get('data', {}).get('is_finished'):
            count = 0
            return True
        elif not resp.get('data').get('is_finished') and count <= 5:
            time.sleep(2)
            return self._get_job_instance_status(task_id)
        else:
            count = 0
            return False

    def get_job_instance_log(self, task_id):
        """
        查询日志
        :param task_id: job_instance_id
        :return:
        """
        if self._get_job_instance_status(task_id):
            resp = self.client.job.get_job_instance_log(
                job_instance_id=task_id,
                bk_biz_id=self.biz_id,
                bk_username='admin'
            )
            ip_logs = resp.get("data")[0].get('step_results')[0].get("ip_logs")
            return ip_logs

        else:
            return False

    def _execute_job(self):
        """
        执行job
        :return:
        """
        steps = self._get_job_steps()
        params = {
            "bk_username": self.username,
            "bk_biz_id": self.biz_id,
            "bk_job_id": self.bk_job_id,
            "steps": steps,
            # "global_vars": global_vars,
            # "bk_callback_url": self.bk_callback_url
        }
        result = self.client.job.execute_job(**params)
        # print result
        if result.get('result'):
            job_instance_id = result.get('data').get('job_instance_id')
            return True, job_instance_id
        else:
            return False, result.get('message')

    def execute_job_and_return(self):
        flag, instance_id = self._execute_job()
        if flag:
            ip_logs = self.get_job_instance_log(instance_id)
            if ip_logs:
                log_content = ip_logs[0].get('log_content')
                return log_content
