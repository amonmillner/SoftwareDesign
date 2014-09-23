'''
Grid maker
'''

def makegrid(x,y,z):
    onebox='+'+'-'*z
    onespace='|'+' '*z
    a=0
    while a < y:
        b = 0
        print onebox*x+'+'
        while b < z:
            print onespace*x+'|'
            b=b+1
        a=a+1
    print onebox*x+'+'