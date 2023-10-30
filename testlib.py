#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:57:18 2023

@author: ruyonga
"""

import sys

def test(did_pass):
    """  Print the results of a test. """
    linenum = sys._getframe(1).f_lineno
    
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
        
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)