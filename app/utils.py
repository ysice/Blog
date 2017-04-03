#!/usr/bin/env python
# -*- coding=utf-8 -*-
# Create by ysicing on 2016/12/13

from app.models import db, Pages, Users, ip2long, long2ip, Config, IP


from six.moves.urllib.parse import urlparse, urljoin
import six
from werkzeug.utils import secure_filename
from functools import wraps
from flask import current_app as app, g, request, redirect, url_for, session, render_template, abort
#from flask_caching import Cache
from flask_cache import Cache
from itsdangerous import Signer, BadSignature
from socket import inet_aton, inet_ntoa, socket
from struct import unpack, pack, error
from sqlalchemy.engine.url import make_url
from sqlalchemy import create_engine


import time
import datetime
import hashlib
import shutil
import requests
import logging
import os
import sys
import re
import time
import smtplib
import email
import tempfile
import subprocess
import urllib
import json


cache = Cache()


def init_logs(app):
    logger_do = logging.getLogger('done')
    logger_logins = logging.getLogger('logins')
    logger_regs = logging.getLogger('regs')

    logger_do.setLevel(logging.INFO)
    logger_logins.setLevel(logging.INFO)
    logger_regs.setLevel(logging.INFO)

    try:
        parent = os.path.dirname(__file__)
    except:
        parent =os.path.dirname(os.path.realpath(sys.argv[0]))

    log_dir = os.path.join(parent, 'logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logs = [
        os.path.join(parent, 'logs', 'done.log'),
        os.path.join(parent, 'logs', 'logins.log'),
        os.path.join(parent, 'logs', 'regs.log')
    ]

    for log in logs:
        if not os.path.exists(log):
            open(log, 'a').close()


def init_errors(app):
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html'), 403

    @app.errorhandler(500)
    def net_error(error):
        return render_template('errors/500.html'), 500

    @app.errorhandler(502)
    def gate_error(error):
        return render_template('errors/502.html'), 502


def init_utils(app):
    app.jinja_env.globals.update(pages=pages)
    app.jinja_env.globals.update(blog_name=blog_name)
    app.jinja_env.globals.update(blog_theme=blog_theme)
    app.jinja_env.globals.update(blog_des=blog_des)
    app.jinja_env.globals.update(blog_key=blog_key)
    app.jinja_env.globals.update(blog_saying=blog_saying)
    app.jinja_env.globals.update(blog_misc=blog_misc)

def authed():
    pass


def ip2long():
    pass


def long2ip():
    pass


@cache.memoize()
def is_setup():
    setup = Config.query.filter_by(key='setup').first()
    if setup:
        return setup.value
    else:
        return False


def is_admin():
    if authed():
        return session['admin']
    else:
        return False

def admins_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('admin'):
            return f(*args, **kwargs)
        else:
            return redirect(url_for('auth.login'))
    return decorated_function


def validate_url():
    pass

@cache.memoize()
def blog_name():
    name = get_config('blog_name')
    return name if name else 'Blog'

@cache.memoize()
def blog_theme():
    theme = get_config('blog_theme')
    return theme if theme else ''

@cache.memoize()
def blog_des():
    description = get_config('blog_des')
    return description if description else 'A flask Blog By Ysicing'

@cache.memoize()
def blog_key():
    keywords = get_config('blog_keys')
    return keywords if keywords else 'Python,运维,Ops,Docker,Linux'

@cache.memoize()
def blog_saying():
    blog_saying = get_config('blog_saying')
    return blog_saying if blog_saying else '当你的才华撑不起你的野心时，就要静心去多读书！'

@cache.memoize()
def blog_misc():
    blog_misc = get_config('blog_misc')
    return blog_misc if blog_misc else '国ICP1314520'

def pages():
    pages = Pages.query.filter(Pages.route != 'index').all()
    return pages

@cache.memoize()
def get_config(key):
    config = Config.query.filter_by(key=key).first()
    if config and config.value:
        value = config.value
        if value and value.isdigit(): #isdigit num yes or no
            return int(value)
        elif value and isinstance(value, six.string_types):
            if value.lower() == 'true':
                return True
            elif value.lower() == 'false':
                return False
            else:
                return value
    else:
        set_config(key, None)
        return None


def set_config(key, value):
    config = Config.query.filter_by(key=key).first()
    if config:
        config.value = value
    else:
        config = Config(key, value)
        db.session.add(config)
    db.session.commit()
    return config

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

def sha512(str1):
    return hashlib.sha512(str1).hexdigest()


def gett_ip():
    pass




