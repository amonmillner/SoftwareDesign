# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 22:51:45 2014

@author: benjamin
"""

def check_fermat(a,b,c,n):
    if n > 2 and (a^n)+(b^n)==(c^n):
         print ("Holy smokes, Fermat was Wrong")
    else:
        print ("no, that doesnt work")
check_fermat(int(raw_input("valor a:")),int(raw_input("valor b:")),int(raw_input("valor c:")),int(raw_input("valor n:")))   
