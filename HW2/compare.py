# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 22:26:06 2014
hw2/compare.py
@author: lauren
"""

def compare(x,y):
    if x >y:
        return 1
    if x == y:
        return 0
    if x<y: 
        return -1
        
compare(1,1)

print compare(2,1)