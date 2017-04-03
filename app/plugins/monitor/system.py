#!/usr/bin/env python
# coding=utf-8 

# Created by ysicing on 2017/1/5

import psutil
import time

def getCpu():
    cpunum = psutil.cpu_count()
    cpunumtime = psutil.cpu_times()
    l=[]
    for i in cpunumtime:
        l.append(i)
    #print(cpunum,cpunumtime,l)
    print(l[0])

while True:
    time.sleep(5)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
    getCpu()