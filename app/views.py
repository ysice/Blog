#!/usr/bin/env python
# -*- coding=utf-8 -*-
# Create by ysicing on 2016/12/13

from flask import current_app as app, render_template, render_template_string, request, redirect, abort, jsonify, json as json_mod, url_for, session, Blueprint, Response, send_file
from app.utils import authed, ip2long, long2ip, is_setup, is_admin, validate_url, get_config, set_config, sha512, gett_ip, cache
from app.models import db, Users, Pages

from jinja2.exceptions import TemplatesNotFound
from passlib.hash import bcrypt_sha256
from collections import OrderedDict


import logging
import os
import re
import sys
import json
import os
import datetime


views = Blueprint('views', __name__)


@views.before_request
def redirect_setup():
    if request.path.startswith("/static"):
        return
    if not is_setup() and request.path != "/setup":
        return redirect(url_for('views.setup'))


@views.route('/setup', methods=['GET', 'POST'])
def setup():
    if not is_setup():
        if not session.get('wslove'):
            session['wslove'] = sha512(os.urandom(10))
        if request.method == 'POST':
            blog_name = request.form['blog_name']
            blog_name = set_config('blog_name', blog_name)

            css = set_config('start', '')

            #admin user
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            admin = Users(name, email,password)
            admin.admin = True
            admin.banned = True
            ## Welcome Page
            page = Pages('index', """
            <div class="container main-container">
            <h3 class="text-center">
                Welcome to Use GoBlog System
            </h3>
            <h4 class="text-center">
                <a href="{0}/admin">GuanLi</a> Your Blog
            </h4>
            </div>
            """.format(request.script_root)
                         )

            #allow/disallow reg
            prevent_registration = set_config('prevent_registration', None)

            #verify emails
            verify_emails = set_config('verify_emails', None)

            mail_server = set_config('mail_server', None)
            mail_port = set_config('mail_port', None)
            mail_tls = set_config('mail_tls', None)
            mail_ssl = set_config('mail_ssl', None)
            mail_username = set_config('mail_username', None)
            mail_password = set_config('mail_password', None)

            setup = set_config('setup', True)

            db.session.add(page)
            db.session.add(admin)
            db.session.commit()
            db.session.close()
            app.setup = False
            with app.app_context():
                cache.clear()
            return redirect(url_for('views.static_html'))
        return render_template('setup.html', wslove=session.get('wslove'))
    return redirect(url_for('views.static_html'))


@views.route('/static/user.css')
def custom_css():
    return Response(get_config("css"), mimetype='text/css')


@views.route("/", defaults={'template': 'home'})
@views.route("/<template>")
def static_html(template):
    try:
        return render_template('%s.html' % template)
    except TemplatesNotFound:
        page = Pages.query.filter_by(route=template).first()
        if page:
            return render_template('page.html', content=page.html)
        else:
            abort(404)


# admin profile setting
