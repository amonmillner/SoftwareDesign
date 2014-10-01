# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 22:13:53 2014

@author: anna
"""

from pattern.web import Twitter, plaintext
import nltk
import re


t = Twitter()
i = None
def rhyme(inp, level): #this is a code I got frome  stack overflow that uses that uses the CMU pronounciation dictionary to generate a list of rhyming words
     entries = nltk.corpus.cmudict.entries() # the rhyme function is not my own work but it is much better than my previous method which involved matching the last 3 letters of the last word in the tweet
     syllables = [(word, syl) for word, syl in entries if word == inp]
     rhymes = []
     for (word, syllable) in syllables:
             rhymes += [word for word, pron in entries if pron[-level:] == syllable[-level:]]
     return set(rhymes)
     
def matchtweets(q):
    tweets=[]
    twords=[]
    owords=[]
    pattn = re.compile('([^\s\w]|_)+') #variable that removes non alphanumerics (but leaves spaces)
    for j in range(50):
         for tweet in t.search(q, start=i, count=400): #gets tweets
             if 't.co' not in tweet.text and '@' not in tweet.text: #takes out links and @s
                 tweet.text=pattn.sub('', tweet.text) #adds to the list of tweets
                 tweets.append(plaintext(tweet.text)) #talkes out non alphanumerics
    tweets=list(set(tweets))#gets rid or repeat tweets
    for tweet in tweets: #set ot tweets to run
        for othertweet in tweets[1:]: #against this set of tweets
            if abs(len(tweet) - len(othertweet)) <= 15 and len(tweet) >=10: #makes sure the tweets are similar in length and more than 10 charachters
                twords = tweet.split() #splits the tweet into a list of the words
                owords = othertweet.split() #ditto
                if twords[-1] != owords[-1] and twords[-1] in rhyme(owords[-1],1): #makes sure it doesn't rhyme the same 2 words, and then uses rhyme to see if the word is in the list of the other word's rhymes
                    print tweet
                    print othertweet
                    print
matchtweets('cat')
