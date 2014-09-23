# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 21:57:53 2014

@author: caleb
"""

def checkfermat(a,b,c,n):
    if ((a**n)+(b**n))!=c**n:
        print 'No, that doesn"t work.'
    else:
        print 'Holy smokes, Fermat was wrong!'