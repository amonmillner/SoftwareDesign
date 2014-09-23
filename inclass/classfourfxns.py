   #Factorial(n): write a function that returns n!
   # sum_integers(x,y): write a function that returns the sum of all integers in the range [x,y]
   # is_prime(n): write a function that returns True iff n is a prime number
   # is_palindrome(x): write a function that returns True iff the string x is a palindrome
   # approximate_e() (challenge problem): write a function that computes the value of e to many decimal places (you should be able to tune the number of decimal places in your program).  Hint: check out the Taylor expansion of the exponential function http://en.wikipedia.org/wiki/Taylor_series, also check out the python module decimal for arithmetic with customizable precision)"""
from math import factorial
from decimal import Decimal

def factorialsoftdes(n):
    """Don't call this factoral(). This name is used by the math module"""
    pass

def sum_integers(x,y):
    pass

def is_prime(n):
    pass

def is_palindrome(x):
    pass

def approximate_e(numdecpoints):
    "Takes an integer input (int() function will take care of non-integer inputs) and outputs "
    multby = numdecpoints + 4
    e_approx = 1*10**multby
    for i in xrange(multby):
        
        e_approx = e_approx + 10**multby*(10**multby)/(10**(multby)*factorial(i+1))
    print e_approx

    eout = str(e_approx/10**3)
    edec = eout[1:-1]


    print 'Your approximation of e is 2.'+edec



approximate_e(5)
