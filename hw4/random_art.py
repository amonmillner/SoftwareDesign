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
    x=random.randrange(0,4,1) #generates random number
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

                        
func1 = ['prod',Build_random_function(3,9),Build_random_function(3,3)] #builds function for red channel
func2 = ['prod',Build_random_function(3,9),Build_random_function(3,3)] #green
func3 = ['prod',Build_random_function(3,9),Build_random_function(3,3)] #blue
print func1
bluh=['prod',['sin_pi',['x']],['sin_pi',['y']]]
print Evaluate_function(bluh,1,1)
def Evaluate_function(f,x,y):
    ''' evaluates the function created in Build_random_function 
    replacing strings with mathematical operators and solving for 2 variables (x,y)
    takes 3 inputs the function you want to evaluate, x, and y
    '''
    if f[0] == 'y': #end condition 1
        return y
    if f[0] =='x': #EC2
        return x
    elif f[0] == 'prod':
        return Evaluate_function(f[1],x,y) * Evaluate_function(f[2],x,y) #multiplies 2 functions
    elif f[0] == 'sin_pi':
        return sin(Evaluate_function(f[1],x,y)) 
    elif f[0] == 'cos_pi':
        return cos(Evaluate_function(f[1],x,y))
    elif f[0] == 'tanh':
        return tanh(Evaluate_function(f[1],x,y)) #hyperbolic tangent
    elif f[0] == 'expm1':
        return (Evaluate_function(f[1],x,y))**2 #e^(x-1)
        
def Remap_value(val, input_start, input_end, output_start, output_end):
    '''remaps a value in one range to an equivalent value in another. Takes 5 inputs val,input_start, input_end, output_start, output_end - 
    val is the value you want remapped,  input_start and input_end are the min and max of the interval val is in. 
    output_start and output_end define the interval you want the new value in.
    '''
    inputrange = input_end - input_start 
    outputrange = output_end - output_start 
    val2= float(val - input_start) / inputrange
    valremapped= output_start + (val2*outputrange)
    return valremapped

im = Image.new("RGB",(350,350)) #generates blank image


r=0 #initial values
g=0
b=0
for x in range(0,349): #columns
    for y in range (0,349): #rows
        r = Evaluate_function(func1,Remap_value(x,0,349,-1,1),Remap_value(y,0,349,-1,1)) #solves the function for 350 values of x between -1 and 1
        g = Evaluate_function(func2,Remap_value(x,0,349,-1,1),Remap_value(y,0,349,-1,1))
        print g
        b = Evaluate_function(func3,Remap_value(x,0,349,-1,1),Remap_value(y,0,349,-1,1))
        im.putpixel((x, y), (int(Remap_value(r,-1,1,0,255)),int(Remap_value(g,-1,1,0,255)),int(Remap_value(b,-1,1,0,255)))) # generates image from function - converting the z values (r,g,b) into ints between 0 and 255
im.save('pixa10',"JPEG") #saves the image generated