#!/usr/bin/env python
# -*- coding=utf-8 -*-
# Create by ysicing on 2016/12/16

import os, random

with open('.blog_secret_key', 'ab+') as secret:
    secret.seek(0)
    key = secret.read()
    if not key:
        key = os.urandom(64)
        # print(key)
        try:
            secret.write(key)
            secret.flush()
        except:
            key = random.sample('01234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*', 64)
            secret.write(key)
            secret.flush()
            # print('xxx',key)


SECRET_KEY = key

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///blog.db'

SQLALCHEMY_TRACK_MODIFICATIONS = False

SESSION_FILE_DIR = "/tmp/flask_session"

SESSION_COOKIE_HTTPONLY = True

PERMANENT_SESSION_LIFETIME = 604800     # 7 days

HOST = ".ysicing.net"

MAILFROM_ADDR = "admail@ysicing.tech"

UPLOAD_FOLDER = os.path.normpath('static/uploads')

TEMPLATES_AUTO_RELOAD = True

CACHE_TYPE = "simple"
if CACHE_TYPE == 'redis':
    CACHE_REDIS_URL = os.environ.get('REDIS_URL')


