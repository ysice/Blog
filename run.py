#!/usr/bin/env python
# -*- coding=utf-8 -*-
# Create by ysicing on 2016/12/13

from app import create_app
app = create_app()
app.run(host="0.0.0.0", port=4000, debug=True, threaded=True)