#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 15:11:03 2017

@author: gfpp
"""

# Ejemplo del video 68 "More Analyzing Complexity"
def genSubsets(L):
    if len(L) == 0:
        return [[]]                 # list of empty list
    smaller = genSubsets(L[:-1])    # all subsets without last element
    extra = L[-1:]                  # create a list of just last element
    new = []
    for small in smaller:
        new.append(small+extra)     # for all smaller solution, add one with last element
    return smaller+new              # combine those with last element and those without
