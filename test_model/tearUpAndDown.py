#! /usr/bin/python
# -*- coding:utf-8 -*-

import unittest

def   setUpModule():
    print('=========setupModule=========')
def  tearDownModule():
    print ("=========tearDownModule=========")
class  TestClass1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "======setUpClass======"
    @classmethod
    def tearDownClass(cls):
        print "======tearDownClass========="
    def setUp(self):
        print "========setup========"
    def tearDown(self):
        print "==========tearDown======"
    def test_a(self):
        print "a"
    def test_b(self):
        print "b"
class TestClass2(unittest.TestCase):
    def test_a(self):
        print ("A")

if __name__ == "__main__":
    unittest.main()

