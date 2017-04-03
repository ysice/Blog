#!/usr/bin/env python
# coding=utf-8 

# Created by ysicing on 2017/1/3

from flask import render_template, request, redirect, abort, jsonify, url_for, session, Blueprint
from app.utils import sha512, authed, admins_only, is_admin, get_config, set_config, cache
from app.models import db, Config, DatabaseError, Pages, Users, IP
from itsdangerous import TimedSerializer, BadTimeSignature
from sqlalchemy.sql import and_, or_, not_
from sqlalchemy.sql.expression import union_all
from sqlalchemy.sql.functions import coalesce
from werkzeug.utils import secure_filename
from socket import inet_aton, inet_ntoa
from passlib.hash import bcrypt_sha256
from flask import current_app as app

import logging
import hashlib
import time
import re
import os
import json
import datetime
import calendar

admin = Blueprint('admin', __name__)

@admin.route('/admin', methods=['GET'])
def admin_view():
    if is_admin():
        return redirect(url_for('admin.adminds'))
    return redirect(url_for('auth.login'))

@admin.route('/admin/web')
@admins_only
def adminds():
    return render_template('admin/web.html')

@admin.route('/admin/config', methods=["POST","GET"])
@admins_only
def admin_config():
    if request.method == "POST":
        blog_name = set_config("blog_name", request.form.get('blog_name', None))
        blog_theme = set_config("blog_theme", request.form.get('blog_theme',None))

    return render_template('admin/config/config.html')

@admin.route('/admin/monitor/<name>')
@admins_only
def admin_monitor(name):
    '''
    monitor
    '''
    if name == 'system':
        ipinfo_i = {}
        ipinfo_j = {}
        ipinfo = IP.query.filter_by(id=IP.query.count()).all()
        in_ipinfo = ipinfo[0].in_ip
        for i in in_ipinfo.split('='):
            print(i,i.split('-'))
            if i:
                ipinfo_i[i.split('-')[0]]=i.split('-')[1]
        ipinfo_j['out_ip'] = ipinfo[0].out_ip
        ipinfo_j['country'] = ipinfo[0].out_country
        ipinfo_j['region'] = ipinfo[0].out_region
        ipinfo_j['city'] = ipinfo[0].out_city
        ipinfo_j['time'] = ipinfo[0].iptime
        return render_template('admin/jk/sys.html',name=name,inip=ipinfo_i,gwip=ipinfo_j)
    elif name == 'blog':
        return render_template('admin/jk/blog.html',name=name)
    else:
        return render_template('admin/jk/status.html',name=name)

@admin.route('/admin/posts/<name>')
@admins_only
def admin_posts(name):
    if name == 'list':
        return render_template('admin/posts/list.html', name=name)
    elif name == 'comment':
        pass
    else:
        return render_template('admin/posts/del.html', name=name)

@admin.route('/admin/terminal')
@admins_only
def admin_terminal():
    '''
    ssh/terminal
    '''
    pass

@admin.route('/skin_config/')
def skin_config():
    return render_template('admin/skin_config.html')


@admin.route('/admin/user/<name>',methods=['GET','POST','PUT','DELETE'])
@admins_only
def admin_user(name):
    #print(name)
    users = Users.query.all()
    print(users)
    if name == 'group':
        return render_template('admin/user/ugroup.html', name=name)
    elif name == 'list':
        if 'id' in request.args:
            print(request.args['id'])
            upuser = Users.query.filter_by(id=request.args['id']).first()
            if upuser:
                return render_template('admin/user/update.html',name=name,users= upuser)
        return render_template('admin/user/ulist.html', name=name, users=users)
    elif name in 'useradd' :
        if request.method == 'GET':
            return render_template('admin/user/add.html',name=name)
        if request.method == 'POST':
            name = request.form.get('username')
            print(name)
            res = Users.query.filter_by(name=name).first()
            if res:
                return render_template('admin/user/add.html',res=res,error='已经存在')
            passowrd = request.form['password']
            email = request.form['email']
            adduser = Users(name=name,password=passowrd,email=email)
            adduser.admin = True
            adduser.banned = True
            adduser.joined = datetime.datetime.now()
            db.session.add(adduser)
            db.session.commit()
            db.session.close()
            return render_template('admin/user/add.html',res='need update',msg='更新完成')
    elif name in 'userdel':
        #if request.method == "post":
        ids = request.values.get('id','')
        for i in ids:
            deluser=Users.query.filter_by(id=int(i)).first()
            db.session.delete(deluser)
        db.session.commit()
        db.session.close()
        return render_template('admin/test/demo.html',res='666')
    elif name in 'update':
        uid = request.args['id']
        print(uid)
        upuser = Users.query.filter_by(id=int(uid)).first()
        if uid == 1:
            return render_template('admin/user/update.html',users=upuser,error='no allow')
        passwd = request.form['password']
        email = request.form['email']
        if passwd:
            #uppasswd = Users(name=upuser.name,
            #                 password=(passwd if passwd else upuser.password),
            #                email=(email if email else upuser.email))
            upuser.password = passwd
        if email:
            upuser.email = email
        db.session.commit()
        #db.session.close()
        uppuser = Users.query.filter_by(id=uid).first()
        return render_template('admin/user/update.html',name=name,users=uppuser,msg='Update successful')
    else:
        print('id=',request.args['id'])
        userinfo = Users.query.filter_by(id=request.args['id']).first()
        return render_template('admin/user/profile.html', name=name,userinfo=userinfo)

'''
@admin.route('/admin/api/<name>', methods=['GET','POST','PUT','DELETE'])
@admins_only
def api_admin(name):
    if name == 'useradd' and request.method == 'POST':
        username = request.form.get('username')
        print(username)
        res=Users.query.filter_by(name=username).first()
        if res:
            return render_template('admin/test/demo.html',res=res)
        return render_template('admin/test/demo.html',res='update')
'''