#!/usr/bin/env python
# coding=utf-8 

# Created by ysicing on 2017/1/3

from flask import render_template, request, redirect, abort, jsonify, url_for, session, Blueprint
from app.utils import sha512, authed, get_config, is_safe_url
from app.models import db, Users
from itsdangerous import TimedSerializer,BadTimeSignature
from passlib.hash import bcrypt_sha256
from passlib.apps import custom_app_context as pwd_context
from flask import current_app as app

import logging
import time
import re
import os
import urllib

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        errors = []
        name = request.form['name']
        iname = Users.query.filter_by(name=name).first()
        if iname:
            try:
                status = bcrypt_sha256.verify(request.form['password'], iname.password)
            except:
                hash = pwd_context.encrypt(request.form['password'])
                status = pwd_context.verify(iname.password, hash)
            if iname and status:
                try:
                    session.regenerate()
                except:
                    pass
                session['username'] = iname.name
                session['id'] = iname.id
                session['admin'] = iname.admin
                session['nonce'] = sha512(os.urandom(10))
                db.session.close()

                logger = logging.getLogger('logins')
                logger.warn("[{0}] {1} logged in".format(time.strftime("%m/%d/%Y %X"),session['username'].encode('utf-8')))

                if request.args.get('next') and is_safe_url(request.args.get('next')):
                    return redirect(request.args.get('next'))
                return redirect(url_for('admin.adminds'))

            else:
                errors.append("Incorrect Username or password .")
                db.session.close()
                return render_template('login.html', errors=errors)

        else:
            errors.append("Incorrect Username or password .")
            db.session.close()
            return render_template('login.html', errors=errors)
    else:
        db.session.close()
        return render_template('login.html')

@auth.route('/logout')
def logout():
    if authed():
        session.clear()
    return redirect(url_for('views.static_html'))