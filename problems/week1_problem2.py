#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 16:17:34 2017

@author: gfpp
"""

# Assume s is a string of lower case characters.
#
# Write a program that prints the number of times 
# the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', 
# then your program should print
#
# Number of times bob occurs is: 2

#s = 'azcbobobegghakl'
s = 'alkjbobalkbobboboiuwobobob'

s1 = 'bob'
l1 = len(s1)
n_s1 = 0

for idx in range(len(s)-l1+1):
    if s[idx:idx+l1] == s1:
        n_s1 += 1
print("Number of times bob occurs is: " + str(n_s1))
