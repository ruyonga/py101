#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:56:24 2023

@author: ruyonga
"""

import random

rng = random.Random()
number = rng.randrange(1, 1000)

guesses = 0

msg = ""

while True:
    guess = int(input(msg + "\n Guess my number between 1 and 1000: "))
    guesses += 1
    
    if guess > number:
        msg = str(guess) + " is too high. \n"
        
    elif guess < number:
        msg = str(guess) + " is too low.\n"
    else:
        break
    
print("\n\nGreat, you got in {0} gueses!\n\n".format(guess))