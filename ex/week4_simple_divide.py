#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:36:07 2017

@author: gfpp
"""

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


# Original definition
#
# This code raises a ZeroDivisionError exception for the 
# following call: fancy_divide([0, 2, 4], 0)
#def simple_divide(item, denom):
#    return item / denom
    
   
def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0