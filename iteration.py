#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:14:09 2023

@author: ruyonga
"""

from testlib import test


def mysum(xs):
    """ Sum all the numbers in teh list xs, and return the total"""

    running_total = 0

    for x in xs:
        running_total = running_total + x

    return running_total


def createtable():
    for x in range(13):
        print(x, "\t", 2**x)

createtable()


"\n"

students = [
    
    ("john", ["compsci", "physics"]), ("vusi", ["math", "compsci", "stats"]),
    ("jess", ["compsci", "accounting", "economics","commonlaw"]),
    ("sarah", ["infosys", "accounting", "economics", "commonlaw"]),
    ("Zuki", ["sociology", "Economics", "Law", "Stats", "Music"])

    ]

for (name, subject) in students:
    print(name, "takes", len(subject), "courses")
    
    for c in subject:
        com = 0
        
        if (c == "compsci"):
            com = com + 1
        print(com)
            




"\n"
test(mysum([1, 2, 3, 4]) == 10)
test(mysum([1.25, 2.5, 1.75]) == 5.5)
test(mysum([1, -2, 3]) == 2)
test(mysum([]) == 0)
test(mysum(range(11)) == 55)
