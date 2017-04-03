#!/usr/bin/env python
# coding=utf-8 

# Created by ysicing on 2017/1/14

from flask_sqlalchemy import SQLAlchemy
from app.models import db,Users,Pages,Config,IP
from app.plugins.monitor import ip

import json
import time
import re
import os
import datetime

'''
查询iapi
key = 15AB40CD51BB672FCE905557119C110EDF1678CA
'''

# user info query func
def uinfo():
    users = Users.query.all()
    return users



#monitor info query func
def jkinfo():
    ipd = ip.get_ip()
    #print(IP.query.count())
    if not IP.query.count() or IP.query.count():
        gw_ip,gw_country,gw_city,gw_ori = ipd['gw'][0],ipd['gw'][1],ipd['gw'][2],ipd['gw'][3]
        try:
            lo = ipd['lo']
            del ipd['lo']
        except:
            lo = '127.0.0.1'
        del ipd['gw']

        #print(ipd,gw_ip,gw_city,gw_country,gw_ori)
        in_ip = []
        for i in ipd:
            in_ip.append(i+'-'+ipd[i]+'=')
        #print(in_ip)
        ip_first=IP(in_ip=''.join(in_ip),out_ip=gw_ip,out_country=gw_country,out_city=gw_city,out_region=gw_ori)
        ip_first.iptime = datetime.datetime.now()
        db.session.add(ip_first)
        db.session.commit()
        db.session.close()
        return
    #in_ip error

    #print(ipd)



#eassy info query func
def wzinfo():
    pass


# loginfo
def loginfo():
    pass


def staticinfo():
    pass


def apinfo():
    pass



jkinfo()
    #time.sleep(86400)
#time.sleep(60)