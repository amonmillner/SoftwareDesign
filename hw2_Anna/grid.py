# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/anna/.spyder2/.temp.py
"""

def grid(x):
    horiz='+ - - - - '
    verti='|         '
    print ('\n'+horiz*x + '+' +( '\n' + verti*x+'|')*4)*x
    print horiz*x

grid(1)
grid(2)
grid(3)
grid(4)
#etc..



