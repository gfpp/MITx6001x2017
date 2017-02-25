#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 15:14:31 2017

@author: gfpp
"""

# Here is code for linear search that uses the fact that a set of elements is 
# sorted in increasing order: 
def search(L, e):
    for i in range(len(L)):
        print(i, ",", L[i], ",", e)
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
    
#  Consider the following code, which is an alternative version of search. 
def newsearch(L, e):
    size = len(L)
    for i in range(size):
        print(i, ",", size-i-1, ",", L[size-i-1], ",", e)
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False
    
L = [1,2,3,4,5,6,7,8,9]

#print(search(L, 3))
#print(newsearch(L, 3))
#
#print(search([], 0))
#print(newsearch([],0))

print(search([], 0))
print(newsearch([],0))

# Which of the following statements is correct? You may assume that each function 
# is tested with a list L whose elements are sorted in increasing order; for 
# simplicity, assume L is a list of positive integers.
#
# A) search and newsearch return the same answers for all L and e.
# B) search and newsearch return the same answers provided L is non-empty.
# C) search and newsearch return the same answers provided L is non-empty and e is in L.
# D) search and newsearch never return the same answers.
# E) search and newsearch return the same answers for lists L of length 0, 1, or 2. correct  <<===
