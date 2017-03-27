#!/usr/bin/env python
# coding=utf-8

"""
author:ysicing
date:2016-08-03
version:3.0beta
"""

from flask import Flask,render_template,url_for,request,flash,session,redirect
from flask_frozen import Freezer
from flask_flatpages import FlatPages,pygmented_markdown,pygments_style_defs
from datetime import datetime,date
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

from config import osinfo,visitor_info

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

"""
预定义
"""
BASE_URL = "https://ysicing.net"
DEBUG = True
FLATPAGES_ROOT = 'content'
FLATPAGES_EXTENSION = '.md'
# FLATPAGES_ENCODING = ''
# FLATPAGES_HITML_RENDERER = ''
FLATPAGES_AUTO_RELOAD = True
POST_DIR = 'posts'
# PAGE_DIR = 'pages'
# PER_PAGE = 3


app = Flask(__name__)
app.config.from_object(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'Hard to guess String'

def get_brow_info():
    getinfo={}
    user_agent = request.headers.get('User-Agent')
    referer = request.headers.get('Referer')
    ip,user = request.remote_addr,request.remote_user
    list_user = ['iPhone','iPad','Android','webOS']
    getinfo['user_agent'] = user_agent
    getinfo['referer'] = referer
    getinfo['ip'] = ip
    getinfo['user'] = user
    getinfo['list_user'] = list_user

    return  getinfo
app.add_template_global(get_brow_info,'visinfo')

@app.context_processor
def url():
    return dict(BASE_URL=BASE_URL)


class SecForm(Form):
    password = StringField('Input Code',validators=[DataRequired()])
    submit = SubmitField('Done')

#@app.route('/pygments.css')
#def py_css():
#    return pygments_style_defs('vim'), 200, {'Content-Type': 'text/css'}

@app.route('/')
def index_pages():
    return render_template('theme/home.html')

@app.route('/posts/',methods=['GET','POST'])
def posts_all():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item: item['date'], reverse=True)
    num = len(posts)
    form = SecForm()
    if form.validate_on_submit():
        passwd = 'hello'
        if form.password.data is not None:
            if passwd != form.password.data:
                flash('error')
                session['post_sec'] = 'error'
            else:
                flash('Loading')
                session['post_sec'] = 'true'
        else:
            flash('deny')
            session['post_sec'] = 'deny'
        return redirect(url_for('posts_all'))
    return render_template('theme/posts.html', posts=posts, postnum=num,form=form,info=session.get('post_sec'))

@app.route('/post/<name>')
def post_single(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    # postinfo=[p for p in flatpages if p.path.startswith(POST_DIR)]
    today = date.today()
    ptime = date(year=today.year, month=today.month, day=today.day)
    return render_template('theme/post.html', post=post, ptime=ptime)

@app.route('/tags/<string:tname>')
def tag(tname):
    tags = tname.lower()
    ikey = ['all']
    allkey = []
    mbkey = {}
    sectag = ['secret','秘密','个人']
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item: item['date'],reverse=True)
    for xkey in posts:
        allkey.append(xkey['tags'].lower())
    for i in allkey:
        if ' ' in i:
            for j in i.split():
                mbkey[j] = mbkey.get(j,0)+1
        else:
            mbkey[i] = mbkey.get(i,0)+1
    return render_template('theme/tag.html',tags=tags.lower(),ikey=ikey,posts=posts,mbkey=mbkey,sectag=sectag)

@app.route('/m/')
def wap():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item: item['date'], reverse=True)
    return render_template('theme/m.html')
@app.route('/admin/')
def admin_home():
    return render_template('admin/ahome.html')

@app.route('/api/<apiname>',methods=['post','get'])
def api_do(apiname):
    user_agent=request.headers.get("User-Agent")
    if apiname=='recent_new':
        new_posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
        new_posts.sort(key=lambda item: item['date'], reverse=True)
        return render_template('theme/api/recent.html', new_posts=new_posts, postnum=min(len(new_posts), 10))
    if apiname=='admin':
        return "show me your code"
    if apiname=='other':
        return render_template('misc/error.html', error='Not support .So sorry!')
    return user_agent

@app.route('/sb/<name>')
def secret_sb_passwd(name):
    pass
    #return render_template()


@app.route('/links/')
def links():
    return render_template("misc/link/links.html")

@app.route('/about/')
def ops_about():
    return render_template("misc/about/about.html")

@app.route('/guestbook/')
def guestbook():
    return render_template("misc/guestbook/guestbook.html")

@app.route('/status/')
def status():
    osinf = osinfo.OS()
    return render_template("misc/status/status.html", osinfo=osinf)

@app.route('/lab/')
def lab():
    return render_template("misc/lab/lab.html")

@app.route('/love/')
def love():
    return render_template("misc/love/love.html")

@app.route('/devops/')
def gt_tj():
    #UC = visitor_info.UC_info()
    return render_template("misc/gt/gt.html")

@app.route('/robots.txt')
def robots():
    return render_template("misc/robots.txt")

@app.route('/sitemap.xml')
def sitemap():
    today = date.today()
    recently = date(year=today.year, month=today.month, day=1)
    posts = [ p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item: item['date'], reverse=True)
    return render_template('misc/sitemap.xml', posts=posts, today=today, recently=recently)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('misc/error.html',error=404)

@app.errorhandler(500)
def int_error(e):
    return render_template('misc/error.html',error=500)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
