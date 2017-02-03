#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 15:20:51 2017

@author: gfpp
"""

testList = [1, -4, 8, 9]
print(testList)

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    

#def timesFive(a):
#    return a*5
#applyToEach(testList, timesFive)  # Example

# Apply to each 1. [1, 4, 8, 9]
#applyToEach(testList, abs)

# Apply to each 2. [2, -3, 9, -8]
#def weird(a):
#    if a+1 < 10:
#        return a + 1
#    else:
#        return -a + 1
#
#applyToEach(testList, weird)

# Apply to each 3. [1, 16, 64, 81]
