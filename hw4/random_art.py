# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 23:26:59 2014

@author: anna
"""
from math import *
import random
import Image

def build_random_function(min_depth,max_depth):#generates a random function using sin, cos, product, 
    '''Generates a nested list with the strings 'prod' 'cos_pi' 'sin_pi' 'expm' 'tanh' 'x' and 'y' 
    Takes 2 inputs min_depth minimum number of levels deep the function can be nested and 
    max_depth number of levels deep the function can be nested
    '''
    x=random.randrange(0,5,1) #generates random number
    if max_depth == 0:
        if x < 2:
            return ["y"]
        else:
            return ["x"]
    else:
        if x == 4:
             return ["prod",build_random_function(min_depth-1,max_depth-1),
                     build_random_function(min_depth-1,max_depth-1)]
        elif x == 3:
            return ["cos_pi",build_random_function(min_depth-1,max_depth-1)]
        elif x == 2:
             return ["sin_pi",build_random_function(min_depth-1,max_depth-1)]
        elif x == 1:
             return ["expm1",build_random_function(min_depth-1,max_depth-1)]
        elif x == 0:
             return ["tanh",build_random_function(min_depth-1,max_depth-1)]
                        

def evaluate_function(f,x,y):
    ''' evaluates the function created in build_random_function 
    replacing strings with mathematical operators and solving for 2 variables (x,y)
    takes 3 inputs the function you want to evaluate, x, and y
    '''
    if f[0] == 'y':
        return y
    elif f[0] =='x':
        return x
    elif f[0] == 'prod':
        return evaluate_function(f[1],x,y) * evaluate_function(f[2],x,y)
    elif f[0] == 'sin_pi':
        return sin(evaluate_function(f[1],x,y)) 
    elif f[0] == 'cos_pi':
        return cos(evaluate_function(f[1],x,y))
    elif f[0] == 'tanh':
        return tanh(evaluate_function(f[1],x,y)) #hyperbolic tangent
    elif f[0] == 'expm1':
        return expm1(evaluate_function(f[1],x,y)) #e^(x-1)


def remap_value(val, input_start, input_end, output_start, output_end):
    '''remaps a value in one range to an equivalent value in another. Takes 5 
    inputs val,input_start, input_end, output_start, output_end - 
    val is the value you want remapped,  input_start and input_end are the min 
    and max of the interval val is in. 
    output_start and output_end define the interval you want the new value in.
    '''
    inputrange = input_end - input_start 
    outputrange = output_end - output_start 
    val2= float(val - input_start) / inputrange
    valremapped= output_start + (val2*outputrange)
    return valremapped


if __name__ == "__main__":
    red = build_random_function(3,6)
    print red
    green = build_random_function(3,4)
    blue = build_random_function(3,8)
    im = Image.new("RGB",(350,350)) #generates blank image
    r = g = b = 0
    for row in range(0,349):
        for col in range (0,349):
            r = evaluate_function(red,remap_value(row,0,349,-1,1),
                                  remap_value(col,0,349,-1,1)) #solves the function for 350 values of x between -1 and 1
            g = evaluate_function(green,remap_value(row,0,349,-1,1),
                                  remap_value(col,0,349,-1,1))
            b = evaluate_function(blue,remap_value(row,0,349,-1,1),
                                  remap_value(col,0,349,-1,1))            
            im.putpixel((row, col), (int(remap_value(r,-1,1,0,255)),
                        int(remap_value(g,-1,1,0,255)),
                        int(remap_value(b,-1,1,0,255)))) # generates image from function - converting the z values (r,g,b) into ints between 0 and 255
    im.save('example1',"JPEG") #saves the image generated