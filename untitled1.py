#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:33:51 2023

@author: ruyonga
"""

import turtle

def draw_multicolor_square(t, sz):
    
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)
        
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)


size = 20

for i in range(15):
    draw_multicolor_square(tess, size) 
    size = size + 10
    tess.forward(10)
    tess.right(18)

wn.mainloop()
turtle.bye()       