#!/usr/bin/env python
# coding=utf-8

'''
author:ysicing
time:2015-12-20
update:2016-3-12
version:2.0beta
'''
import sys, os, fnmatch, random
from flask import Flask, render_template, request, Markup, abort, redirect, url_for, session
from flask_frozen import Freezer
from flask_flatpages import FlatPages, pygments_style_defs
from datetime import date, datetime
from flask.ext.moment import Moment
from flask.ext.paginate import Pagination
from werkzeug.contrib.cache import MemcachedCache

BASE_URL = "https://ysicing.net"
DEBUG = True
FLATPAGES_ROOT = 'content'
FLATPAGES_EXTENSION = '.md'
# FLATPAGES_ENCODING = ''
# FLATPAGES_HITML_RENDERER = ''
FLATPAGES_AUTO_RELOAD = True
POST_DIR = 'posts'
PAGE_DIR = 'pages'
PER_PAGE = 3


app = Flask(__name__)
app.config.from_object(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
moment = Moment(app)
# cache = MemcachedCache(app.config['MEMCACHED_SERVER'])


def get_num():
    return random.randint(1, 10)
app.add_template_global(get_num, 'get_num')


def api():
    apione = {}
    user_agent = request.headers.get('User-Agent')
    ip = request.remote_addr
    apione['user_agent'] = user_agent
    apione['ip'] = ip
    return apione
app.add_template_global(api, 'ysapi')


@app.route('/api', methods=['GET', 'POST'])
def micapi():
    if request.method == 'GET':
        return redirect(url_for('love'))
    else:
        return redirect(url_for('posts'))


@app.context_processor
def blog_url():
    return dict(BASE_URL=BASE_URL)    # domain,you can write your own domain name


@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('friendly'), 200, {'Content-Type': 'text/css'}
'''
more: https://help.farbox.com/pygments.html
u a free to choose one!
'''


@app.route('/')
def home():
    hposts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    hposts.sort(key=lambda item: item['date'], reverse=True)
    # rannum = random.randint(1,10)
    return render_template('theme/home.html', posts=hposts, postsnum=min(len(hposts), 10))


@app.route('/links')
def link():
    return render_template('theme/links.html')


@app.route('/ops/')
def ops():
    return render_template('theme/ops.html')


@app.route('/love/',methods=['GET','POST'])
def love():
    if 'ice' in session:
        return redirect('theme/love.html', love_you='Allow anything')
    else:
        return render_template('theme/love.html', love_you='Deny By YsiCing GG')


@app.route('/wiki/')
def wiki():
    return render_template('theme/wiki.html')


@app.route('/tags/<string:name>')
def tags(name):
    tags = name.lower()
    ikey = ['all']
    allkey = []
    mbkey = {}
    # tagged = [p for p in flatpages if tags in p.meta.get('tags',[])]
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item: item['date'], reverse=True)
    for xkey in posts:
        allkey.append(xkey['tags'].lower())
    for i in allkey:
        mbkey[i] = mbkey.get(i, 0)+1
    return render_template('theme/tags.html', tags=tags.lower(), ikey=ikey, posts=posts, mbkey=mbkey)


@app.route("/posts/")
def posts():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item: item['date'], reverse=True)
    return render_template('theme/posts.html', posts=posts)


@app.route("/posts/<name>")
def post(name):
    path = '{}/{}'.format(POST_DIR,name)
    post = flatpages.get_or_404(path)
    # postinfo=[p for p in flatpages if p.path.startswith(POST_DIR)]
    today = date.today()
    ptime = date(year=today.year, month=today.month, day=today.day)
    return render_template('theme/post.html', post=post, ptime=ptime)


@app.route("/about-me")
def author():
    return render_template('theme/about-me.html')


@app.route('/robots.txt')
def robots():
    return render_template('sys/robots.txt')


@app.route('/sitemap.xml')
def sitemap():
    today = date.today()
    recently = date(year=today.year, month=today.month, day=1)
    # posts = [p for p in flatpages if p.path.startswitch(POST_DIR)]
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item: item['date'], reverse=True)
    return render_template('sys/sitemap.xml', posts=posts, today=today, recently=recently)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('sys/404.html')


@app.errorhandler(500)
def int_error(e):
    return render_template('sys/500.html')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', port=8080, debug=True)
