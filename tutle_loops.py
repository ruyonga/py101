#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 16:10:04 2023

@author: ruyonga
"""

import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

for c in ["yellow", "red", "purple", "blue"]:
    alex.color(c)
    alex.forward(90)
    alex.left(50)
    alex.right(50)

    

    
  
    
wn.mainloop()
turtle.bye()