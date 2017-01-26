#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 16:13:03 2017

@author: gfpp
"""

# Assume s is a string of lower case characters.
#
# Write a program that counts up the number of vowels 
# contained in the string s. Valid vowels are: 'a', 'e', 
# 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', 
# your program should print:
#
# Number of vowels: 5

#s = 'azcbobobegghakl'
s = 'hello world'
numVowels = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        numVowels += 1
print("Number of vowels: " + str(numVowels))
        

# Paste your code into this box 
#numVowels = 0
#for letter in s:
#    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
#        numVowels += 1
#print("Number of vowels: " + str(numVowels))