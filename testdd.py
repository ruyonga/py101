#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 16:02:12 2023

@author: ruyonga
"""

from testlib import test

def absolute_value(x):

    return abs(x)

def test_suite():
    """ Run the suite for code in this """
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)
    
    
test_suite()