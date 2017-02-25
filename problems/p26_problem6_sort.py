#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 15:21:22 2017

@author: gfpp
"""

# Answer the questions below based on the following sorting function. 
# If it helps, you may paste the code in your programming environment. 
# Study the output to make sure you understand the way it sorts. 

def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
        #for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
    


L = [4,8,9,5,1,3,0,6,2,7]
swapSort(L)

# Does this function sort the list in increasing or decreasing order? 
# (items at lower indices being smaller means it sorts in increasing order, and vice versa) 