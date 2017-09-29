# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:40:57 2017

@author: Risa
"""
#returns the total number of children of A and B combined
#returns -1 is the total number exceeds 4
def numOfKids(numArequest, numBaccept):
    # tot = numBaccept + numArequest
    if (numArequest<=numBaccept):
        return 1
    else:
        return 0

