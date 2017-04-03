#!/usr/bin/env python
# coding=utf-8
# Created by ysicing on 17-1-24

'''
blog:
ip: get server ip
'''

import os
import json
import sys
import requests
import re
import time
import datetime

def get_ip():
    if sys.platform.lower() == 'linux':
        ip = {}
        try:
            get_ip = os.popen("sudo ifconfig -a | grep inet | grep -v inet6 | awk '{print $2}'").read()
            get_if = os.popen("sudo ifconfig -a | grep flags |awk -F ':' '{print $1}'").read()
        except:
            get_ip = os.popen("ifconfig -a | grep inet | grep -v inet6 | awk '{print $2}'").read()
            get_if = os.popen("ifconfig -a | grep flags |awk -F ':' '{print $1}'").read()
        for i in range(len(get_ip.strip().split('\n'))):
            ip[get_if.strip().split('\n')[i]] = get_ip.strip().split('\n')[i]
        get_out_json = requests.get("http://ipinfo.io/json").text
        print(get_out_json)
        try:
            get_out = json.loads(get_out_json)
            ip['gw'] = get_out['ip'], get_out['country'], get_out['region'], get_out['city']
            #print(ip)
        except:
            #print(type(get_out_json), get_out_json)
            return type(get_out_json)
        return ip