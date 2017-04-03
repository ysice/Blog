#!/usr/bin/env python
# coding=utf-8 

# Created by ysicing on 2017/1/7

'''
api接口
ysbot 处理外部数据
ysapi 处理系统数据

'''

from flask import Flask,request,render_template,Blueprint,url_for
from flask import current_app as apiapp
import json
import os
import time
import app.iapi
from app.models import db,IP

api = Blueprint('api',__name__)

@api.route('/ysbot/<name>',methods=['GET','POST'])
def ysbot(name):
    return 'ysbot'

@api.route('/iapi/<name>', methods=['GET','POST'])
def iapi(name):
    if name=='ip':
        ipinfo = IP.query.all()
        demo = ipinfo[len(ipinfo)-1]
        print(type(ipinfo[0]))
        ipinfo1=IP.query.filter_by(out_ip=''.join(ipinfo[0])).first()
        return render_template('admin/test/demo.html',res=ipinfo1[0])
    return 'api',name

@api.route('/test')
def mytest():
    return '404'

try:
    apiapp.add_template_global(iapi.uinfo,'uinfo')
    apiapp.add_template_global(iapi.jkinfo,'jkinfo')
    apiapp.add_template_global(iapi.wzinfo,'wzinfo')
    apiapp.add_template_global(iapi.loginfo,'loginfo')
    apiapp.add_template_global(iapi.staticinfo,'sinfo')
    apiapp.add_template_global(iapi.apinfo,'apinfo')
except:
    apiapp.jinja_env.globals['uinfo'] = app.iapi.uinfo

