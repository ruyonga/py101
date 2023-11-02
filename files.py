#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 16:11:36 2023

@author: ruyonga
"""

myfile = open("test.txt", "w")

myfile.write("My first file written with python")
myfile.write("---------------------------------")
myfile.write("hello world")
myfile.close()