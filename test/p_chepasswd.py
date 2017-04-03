#!/usr/bin/env python
# coding=utf-8 

# Created by ysicing on 2016/12/28

import unittest
from app.plugins import chepasswd as check

class TestCheckPassword(unittest.TestCase):

    def test_regular(self):
        rv = check.password('qwerty')
        self.assertTrue(repr(rv) == 'simple')
        self.assertTrue('GZ' in rv.msg)

    def test_common(self):
        rv = check.password('password')
        self.assertTrue(repr(rv) == 'simple')
        self.assertTrue('CJ' in rv.msg)

    def test_medium(self):
        rv = check.password('tdAdddddd')
        self.assertTrue(repr(rv) == 'medium')
        self.assertTrue('BGQ' in rv.msg)

    def test_strong(self):
        rv = check.password('aWe.1236')
        self.assertTrue(repr(rv) == 'Strong' )
        self.assertTrue('WM' in rv.msg)

if __name__ == '__main__':
    unittest.main()