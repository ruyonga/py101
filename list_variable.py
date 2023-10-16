#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 16:29:32 2023

@author: ruyonga
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 16:10:04 2023

@author: ruyonga
"""

import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
clrs =  ["yellow", "red", "purple", "blue"]

for c in clrs:
    alex.color(c)
    alex.forward(50)
    alex.forward(50)
    alex.right(270)    #what angle to turn

     
  
    
wn.mainloop()
turtle.bye()