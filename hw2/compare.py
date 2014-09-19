# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 00:17:54 2014

@author: benjamin
"""
x=int(raw_input("x="))
y=int(raw_input("y="))



def compare(x,y):
    if x > y:
        return ("1")
    if x==y:
        return("0")
    if x < y:
        return("-1")
print compare(x,y)