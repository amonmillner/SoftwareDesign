# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 14:36:03 2014

@author: caleb
"""


def in_between(x,y,z):
    if type(x) not in [int,float] or type(y) not in [int,float] or type(z) not in [int,float]:
        print 'Give me numbers or get the fuck off my lawn. Bitch.'
        return
    elif x < y and y < z:
        print 'I guess thats true. Whats your point, moron?'
    else:
        print 'Not even a little. Do me a favor and stay in school, okay? Dont chew the furniture on the way out'
        