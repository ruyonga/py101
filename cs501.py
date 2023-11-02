#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 10:37:27 2023

@author: ruyonga
"""
words = set()

def check(word):
    if word.lower() in words:
        return True
    
    else:
        
        return False

def load(dictionary):
    file = open(dictionary, "r")
    for line in file:
        
        word = line.rstrip()
        
        words.add(word)
        
    close(file)
    
    return True


def size():
    return len(words)


def unload():
    return True

def close(file):
    file.close()
    