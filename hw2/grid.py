## grid.py ##

def drawhorizsect(cols):
    """Draws a horizontal grid element using ASCII characters.
    Takes an integer as input (number of desired columns)"""

    line = ' _ ' * 4
    print '+',
    for i in xrange(cols):
        print line,'+',
    print '\n'
    

def drawvertsect(cols):
    """Draws a vertical grid element using ASCII characters.
    Takes an integer as input (number of desired columns)"""

    for h in xrange(4): # Height of each cell is 4
        print '|',
        for i in xrange(cols):
            print ' '*13 +'|',
        print '\n'


def drawgrid(rows,cols):
    """Draws a grid using ASCII characters. You must
    input the desired size of the table by passing in
    two integers--the number of rows [rows] and the 
    number of columns [cols]"""

    for i in xrange(rows):
        drawhorizsect(cols)
        drawvertsect(cols)
    drawhorizsect(cols)
        

drawgrid(2,2)   # Question 3.5.1: Draws a 2x2 grid

print '\n'*5

drawgrid(4,4)   # Question 3.5.2: Draws a 4x4 grid