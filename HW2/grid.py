# -*- coding: utf-8 -*-
"""
hw2/grid.py
Created on Mon Sep 15 21:45:35 2014

@author: lauren
"""


#1

def grid (size):
    row = "+" + "-"*4
    row2= "|" + " "*4
    
    print (row*size + "+" "\n" + ((row2)*size + "|"+"\n")*4) * size,
    print row*size + "+" 


grid(16)
















