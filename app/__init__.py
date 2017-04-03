#!/usr/bin/env python
# -*- coding=utf-8 -*-
# Create by ysicing on 2016/12/13

from flask import Flask, Blueprint, render_template, request, redirect, abort, session, jsonify, json as json_mod, url_for
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler
from flask_session import Session
from sqlalchemy_utils import database_exists, create_database
from jinja2 import FileSystemLoader, TemplatesNotFound
from app.utils import get_config, set_config, cache
#from flask_cache import Cache
import os
import sqlalchemy
from sqlalchemy.engine.url import make_url
from sqlalchemy.exc import OperationalError
import warnings
from flask.exthook import ExtDeprecationWarning
#from flask.ext.moment import Moment

# fixed Warnings
# http://stackoverflow.com/questions/38079200/how-can-i-disable-extdeprecationwarning-for-external-libs-in-flask
warnings.simplefilter('ignore', ExtDeprecationWarning)


class BlogthemeLoader(FileSystemLoader):
    def get_source(self, environment, template):
        if template.startswith('admin/'):
            return super(BlogthemeLoader, self).get_source(environment, template)
        theme = get_config('blog_theme')
        template = "/".join([theme, template])
        return super(BlogthemeLoader, self).get_source(environment, template)


def create_app(config='app.config'):
    app = Flask(__name__)
    with app.app_context():
        app.config.from_object(config)
        app.jinja_loader = BlogthemeLoader(os.path.join(app.root_path, app.template_folder), followlinks=True)

        from app.models import db, Users

        url = make_url(app.config['SQLALCHEMY_DATABASE_URI'])
        if url.drivername == 'postgres':
            url.drivername = 'postgresql'

        db.init_app(app)

        try:
            if not (url.drivername.startswith('sqlite') or database_exists(url)):
                create_database(url)
            db.create_all()
        except OperationalError:
            db.create_all()
        else:
            db.create_all()

        app.db = db
        #cache = Cache()
        cache.init_app(app)
        app.cache = cache

        #moment = Moment(app)

        if not get_config('blog_theme'):
            set_config('blog_theme', 'goblog')

        from app.views import views
        from app.utils import init_logs, init_errors, init_utils
        from app.posts import blog
        from app.admin import admin
        from app.auth import auth
        from app.api import api

        init_utils(app)
        init_errors(app)
        init_logs(app)


        try:
            app.register_blueprint(views)
            app.register_blueprint(blog)
            app.register_blueprint(admin)
            app.register_blueprint(auth)
            app.register_blueprint(api)

        except:
            app.register_blueprint(views)

        # app.register_blueprint(admin)
        return app