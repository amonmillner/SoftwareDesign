# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 23:26:59 2014

@author: anna
"""
i=5
from math import *
import random
import Image

def Build_random_function(min_depth,max_depth):#generates a random function using sin, cos, product, 
    '''Generates a nested list with the strings 'prod' 'cos_pi' 'sin_pi' 'expm' 'tanh' 'x' and 'y' 
    Takes 2 inputs min_depth minimum number of levels deep the function can be nested and 
    max_depth number of levels deep the function can be nested
    '''
    x=random.randrange(0,4,1)
    if max_depth == 0:
        if x < 2:
            return ["y"]
        else:
            return ["x"]
    else:
        if x == 4:
             return ["prod",Build_random_function(min_depth-1,max_depth-1),Build_random_function(min_depth-1,max_depth-1)]
        elif x == 3:
            return ["cos_pi",Build_random_function(min_depth-1,max_depth-1)]
        elif x == 2:
             return ["sin_pi",Build_random_function(min_depth-1,max_depth-1)]
        elif x == 1:
             return ["expm1",Build_random_function(min_depth-1,max_depth-1)]
        elif x == 0:
             return ["tanh",Build_random_function(min_depth-1,max_depth-1)]

                        
func1 = ['prod',Build_random_function(3,9),Build_random_function(3,3)]
func2 = ['prod',Build_random_function(3,9),Build_random_function(3,3)]
func3 = ['prod',Build_random_function(3,9),Build_random_function(3,3)]
print func1
bluh=['prod',['sin_pi',['x']],['sin_pi',['y']]]
print Evaluate_function(bluh,1,1)
def Evaluate_function(f,x,y):
    ''' evaluates the function created in Build_random_function 
    replacing strings with mathematical operators and solving for 2 variables (x,y)
    takes 3 inputs the function you want to evaluate, x, and y
    '''
    if f[0] == 'y':
        return y
    if f[0] =='x':
        return x
    elif f[0] == 'prod':
        return Evaluate_function(f[1],x,y) * Evaluate_function(f[2],x,y)
    elif f[0] == 'sin_pi':
        return sin(Evaluate_function(f[1],x,y))
    elif f[0] == 'cos_pi':
        return cos(Evaluate_function(f[1],x,y))
    elif f[0] == 'tanh':
        return tanh(Evaluate_function(f[1],x,y))
    elif f[0] == 'expm1':
        return expm1(Evaluate_function(f[1],x,y))

im = Image.new("RGB",(350,350))


r=0
g=0
b=0

for y in range(0,349):
    for x in range (0,349):
        r = Evaluate_function(func1,float(x)*2.0/349.0-1.0,float(y)*2.0/349.0-1.0)
        g = Evaluate_function(func2,float(x)*2.0/349.0-1.0,float(y)*2.0/349.0-1.0)
        b = Evaluate_function(func3,float(x)*2.0/349.0-1.0,float(y)*2.0/349.0-1.0)
        im.putpixel((x, y), (int(((r+1)*255)/2),int(((g+1)*255)/2),int(((b+1)*255)/2)))
im.save('pixa10',"JPEG")