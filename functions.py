#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:25:43 2023

@author: ruyonga
"""

import turtle
turtle.clear()

def draw_square(t, sz):
    """Make turtle t draw a square of sz """
    
    for i in range(4):
        t.forward(sz)
        t.left(90)
        
        
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

alex = turtle.Turtle()
draw_square(alex, 50)
wn.mainloop()
turtle.bye()