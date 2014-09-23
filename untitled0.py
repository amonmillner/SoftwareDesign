# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 13:41:57 2014

@author: pinar
"""


#brings in the tools that we want to use.
from pattern.web import *
from random import randint
import re
def scrape():
"""Uses Pattern's URL download function to pull HTML code from the website listed below"""
random_50_fortunes = plaintext(URL('http://www.fortunecookiemessage.com/archive.php?start='+str(randint(0,16)*50)).download())
#creates a list from the large plaintext grab, making new list entries for each newline in the page
fortune_list = random_50_fortunes.split('\n\n')
#one way to traverse a list looking for content - enumerate is used to capture the size of the list in this case
for i, j in enumerate(fortune_list):
#looking for the start of the actual fortunes on the page
if 'Fortune Cookie Quotes' in j and '\n' in j:
starter = i+1
#looking for the end of the actual fortunes on the page
if 'Total quotes in our database' in j:
ender = i
#removing webpage content before and after the fortunes
fortune_list = fortune_list[starter:ender]
#printing the random quote each time we run the program
print '\n' + fortune_list[randint(0,(len(fortune_list)-1))] + '\n'
scrape()