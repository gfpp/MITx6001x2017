#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 16:25:00 2017

@author: gfpp
"""

# Write a program that prints the longest substring of s in which the letters 
# occur in alphabetical order. 
# For example, if 
# s = 'azcbobobegghakl', 
# then your program should print
# Longest substring in alphabetical order is: beggh

#s = 'eieioa'
#s = 'eieioaeiou'
#s = 'eieioaeiouaeiou'

# Test
#s = 'azcbobobegghakl'
s = 'abcbcd'

def is_order(s):
  for i in range(len(s)-1):
    if s[i] > s[i+1]:
      return False
  return True

max_len = 1
max_s = s[0]

for i in range(len(s)-1):
  for j in range(i,len(s)+1):
    if is_order(s[i:j]) and len(s[i:j]) > max_len:
      max_len = len(s[i:j])
      max_s = s[i:j]
	
print("Longest substring in alphabetical order is: " + max_s)
