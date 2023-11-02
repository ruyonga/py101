#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 16:22:54 2023

@author: ruyonga
"""

f = open("f.txt", "r")

xs = f.readlines()

f.close()

xs.sort()
g = open("sorted.txt", "w")

for v in xs:
    g.write(v)
    
g.close()