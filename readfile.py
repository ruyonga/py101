#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 16:18:34 2023

@author: ruyonga
"""

mynewhandle = open("test.txt", "r")
while True:
    theline = mynewhandle.readline()
    
    if len(theline) == 0:
        break
    
    print(theline, end = "")
    
    
mynewhandle.close()