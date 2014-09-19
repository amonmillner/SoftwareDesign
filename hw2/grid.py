# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 22:21:14 2014

@author: benjamin
"""


def row(i):
    while i > 0:    
        print '+ - - - -',
        i = i - 1

def coloumn(i):
    while i > 0:
        print '|        ',
        i = i - 1

def grid(i):
    x = i
    while x > 0:    
        row(i)
        print '+'
        n = 4
        while n > 0:
            coloumn(i)
            print '|'
            n = n - 1
        x = x - 1
    row(i)
    print '+'

x = int(raw_input('x='))

grid(x)
