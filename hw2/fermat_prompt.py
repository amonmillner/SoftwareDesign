# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 22:02:55 2014

@author: caleb
"""

from check_fermat import checkfermat

def fermatprompt():
    x=raw_input('A?\n')
    y=raw_input('B?\n')
    z=raw_input('C?\n')
    v=raw_input('N?\n')
    
    a=int(x)
    b=int(y)
    c=int(z)
    n=int(v)
    
    print 'Calculating...'

    checkfermat(a,b,c,n)