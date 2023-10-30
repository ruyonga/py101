#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:57:02 2023

@author: ruyonga
"""

def printPrimeNumber(p0):
    i = 0
  
    while(True):
        
        flag = 1
        
        x = pow(2, i)
        
        p1 = x  * p0 + (x - 1);
        
        for k in range(2, p1):
            if (p1 % k == 0):
                flag = 0
                
                break
        if(flag == 0):
            break
        
        print(p1, end = " ")
        i  += 1
        

p0 = 47
printPrimeNumber(p0)