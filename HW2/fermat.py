# -*- coding: utf-8 -*-

"""
hw2/fermat.py
Created on Mon Sep 15 22:07:28 2014

@author: lauren
"""

#1
def check_fermat(a,b,c,n):

    if (c**n) == (a**n) + (b**n):
        print 'Holy Smokes, Fermat was wrong!'
    else:
        print 'No, that doesnt work'
    


#2

def inputs():
    a = raw_input('Value a?')
    b = raw_input('Value b?')
    c = raw_input('Value c?')
    n = raw_input('Value n?')
    return a,b,c,n





nums = inputs()
print nums


check_fermat(int(nums[0]),int(nums[1]),int(nums[2]),int(nums[3]))
