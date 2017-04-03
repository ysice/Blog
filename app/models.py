#!/usr/bin/env python
# -*- coding=utf-8 -*-
# Create by ysicing on 2016/12/13

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import DatabaseError
from sqlalchemy.sql import func

from socket import inet_aton, inet_ntoa
from struct import unpack, pack, error as struct_error
from passlib.hash import bcrypt_sha256


import datetime
import hashlib
import json


def sha512(string):
    return hashlib.sha512(string).hexdigest()


def ip2long(ip):
    return unpack('!i', inet_aton(ip))[0]


def long2ip(ip_int):
    try:
        return inet_ntoa(pack('!1', ip_int))
    except struct_error:
        return inet_ntoa(pack('!I', ip_int))


db = SQLAlchemy()


class Pages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route = db.Column(db.String(100), unique=True)
    html = db.Column(db.Text)

    def __init__(self, route, html):
        self.route = route
        self.html = html

    def __repr__(self):
        return "<Pages {0} for Blog {1}>".format(self.route, self.html)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    website = db.Column(db.String(128))
    banned = db.Column(db.Boolean, default=False)
    verified = db.Column(db.Boolean, default=False)
    admin = db.Column(db.Boolean, default=False)
    joined = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.name


class Config(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.Text)
    value = db.Column(db.Text)

    def __init__(self, key, value):
        self.key = key
        self.value = value

class IP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    in_ip = db.Column(db.String(100))
    out_ip = db.Column(db.String(100))
    out_country = db.Column(db.Text)
    out_region = db.Column(db.Text)
    out_city = db.Column(db.Text)
    iptime = db.Column(db.DateTime)

    def __init__(self,in_ip,out_ip,out_country,out_region,out_city):
        self.in_ip = in_ip
        self.out_ip = out_ip
        #self.iptime = iptime
        self.out_city = out_city
        self.out_country =out_country
        self.out_region = out_region

    def __repr__(self):
        return '{0} {1} {2} {3} {4} {5}'.format(self.out_ip,self.out_city,self.out_region,self.out_country,self.in_ip,self.iptime)

