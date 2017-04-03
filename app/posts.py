#!/usr/bin/env python
# coding=utf-8 

# Created by ysicing on 2016/12/26

from flask import render_template, request , abort, redirect, url_for, Blueprint, session
from flask_frozen import Freezer
from flask_flatpages import FlatPages, pygmented_markdown, pygments_style_defs
from flask_moment import Moment
from datetime import datetime, date
from flask import current_app as app
from jinja2.exceptions import TemplateNotFound
from app.models import Pages
from flask import Markup

import os
import re
import time
import sys
import markdown

try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

FLATPAGES_ROOT = 'content'
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ENCODING = 'utf8'
FLATPAGES_AUTO_RELOAD = True
POST_DIR = 'posts'
WIKI_DIR = 'wiki'
app.config.from_object(__name__)

flatpages = FlatPages(app)
freezer = Freezer(app)
moment = Moment(app)

blog = Blueprint('blog', __name__)



#@app.route('/pygments.css')
#def py_css():
#    return pygments_style_defs('vim'), 200, {'Content-Type': 'text/css'}

def get_posts():
    try:
        mypost = [p for p in flatpages if p.path.startwith(POST_DIR)]
    except:
        mypost = [p for p in flatpages if p.path]
    #print(posts)
    try:
        mypost.sort(key=lambda item: item['date'], reverse=True)
    except:
        mypost = sorted(mypost, reverse=True, key=lambda p:p['date'])

    return mypost

app.add_template_global(get_posts, 'mdpost')


@blog.route('/posts', methods=['GET'])
def posts():
    try:
        posts = [p for p in flatpages if p.path.startwith(POST_DIR)]
    except:
        posts = [p for p in flatpages if p.path]
    print(posts)
    try:
        posts.sort(key=lambda item: item['date'], reverse=True)
    except:
        posts = sorted(posts, reverse=True, key=lambda p:p['date'])
    num = len(posts)
    print(num)
    return render_template('posts.html', posts = posts)


@blog.route('/post/<name>', methods=['GET'])
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    ipost = [p for p in flatpages if p.path]
    ipost = sorted(ipost, reverse=True, key=lambda p: p['date'])
    postinfo = {}
    postindex = ipost.index(post)
    pre = None if postindex == 0 else ipost[postindex - 1]
    nex = None if postindex == len(ipost)-1 else ipost[postindex + 1]
    postinfo['pre'] = pre
    postinfo['nex'] = nex
    today = date.today()
    ptime = date(year=today.year, month=today.month, day=today.day)
    #path ="<Page '{0}'>".format(path)
    #post.html = Markup(markdown.markdown(post.html,['codehilite']))
    return render_template('post.html', post=post, ptime=ptime, posts=ipost, postinfo=postinfo )


@blog.route('/tag/<string:tag>')
def tag(tag):
    tag = tag.lower()
    allkey=[]
    tagdict={}
    print(tag)
    path = '{}/{}'.format(POST_DIR, '')
    posts = [p for p in flatpages if p.path]
    #posts = [p for p in flatpages if tag in p.meta.get('tags', [])]
    for xkey in posts:
        print(xkey)
        print(xkey['tags'])
        allkey.append(xkey['tags'])
    print('all:',allkey)
    for i in allkey:
        if type(i) is list:
            for j in i:
                #j = j.lower()
                tagdict[j] = tagdict.get(j,0) + 1
        else:
            #i = i.lower()
            tagdict[i] = tagdict.get(i,0) + 1
    return render_template('tag.html', tagdict=tagdict, tag=tag,posts=posts)



