# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 23:26:59 2014

@author: anna
"""
def check_fermat():
    print ('a,b,c,n')
    x=raw_input()
    
    if int(x[0])**int(x[3]) +int(x[1])**int(x[3]) != int(x[2])**int(x[3]):
        print 'no, that dosent work'
        
    else:
            print 'Holy smokes, Fermat was wrong!'

check_fermat()