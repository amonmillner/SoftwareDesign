## fermat.py ##

def checkfermat(a,b,c,n):
    flt = a**n + b**n - c**n
    
    if flt == 0:
        print 'Holy smokes, Fermat was wrong!'
        print 'Please write to the following address:\n'
        print 'The Nobel Foundation\nP.O. Box 5232\nSE-102 45 Stockholm, Sweden'
    else:
        print 'No, that doesn\'t work.'
        print '(Fermat\'s Last Theorem holds)'


def testfermat():
    print 'Fermat\'s Last Theorem states that no set of positive integers a, b, and c can satisfy the expression'
    print 'a^n + b^n = c^n\n\'n\' is an any value greater than two. This function will allow you to',
    print 'test Fermat\'s Last Theorem with values of your choosing.\nPlease enter a positive integer for \'a\':'
    while True:
        a_check = raw_input('a = ')
        try:
            a = int(a_check)
        except ValueError:
            print "\'a\' must be a positive integer. Please enter a positive integer for \'a\'."
        else:
            if a < 1:
                print"\'a\' must be a positive integer. Please enter a positive integer for \'a\'."
            else:
                break
    print 'Please enter a positive integer for \'b\':'
    while True:
        b_check = raw_input('b = ')
        try:
            b = int(b_check)
        except ValueError:
            print "\'b\' must be a positive integer. Please enter a positive integer for \'b\'."
        else:
            if b < 1:
                print"\'b\' must be a positive integer. Please enter a positive integer for \'b\'."
            else:
                break
    print 'Please enter a positive integer for \'c\':'
    while True:
        c_check = raw_input('c = ')
        try:
            c = int(c_check)
        except ValueError:
            print "\'c\' must be a positive integer. Please enter a positive integer for \'c\.'"
        else:
            if c < 1:
                print"\'c\' must be a positive integer. Please enter a positive integer for \'c\'."
            else:
                break
    print 'Please enter a value greater than 2 for \'n\':'
    while True:
        n_check = raw_input('n = ')
        try:
            n = float(n_check)
        except ValueError:
            print "\'n\' must be a value greater than 2. Please enter a value greater than 2 for \'n\'."
        else:
            if n <= 2:
                print"\'n\' must be a value greater than 2. Please enter a value greater than 2 for \'n\'."
            else:
                break
    print '\nSeeing if %d^%f + %d^%f = %d^%f ...\n\n' % (a,n,b,n,c,n)
    checkfermat(a,b,c,n)                


checkfermat(3,4,5,2)

testfermat()