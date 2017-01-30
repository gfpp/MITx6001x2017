#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:19:51 2017

@author: gfpp
"""

# A regular polygon has n number of sides. Each side has length s.
#
# * The area of a regular polygon is: (0.25*n*s**2 / tan(pi/n))
# * The perimeter of a polygon is: length of the boundary of the polygon
#
# Write a function called polysum that takes 2 arguments, n and s. 
# This function should sum the area and square of the perimeter of 
# the regular polygon. 
# The function returns the sum, rounded to 4 decimal places.

# For using pi value and tan function
import math

def polysum(n, s):
    """
    Input: n, number of sides of the polygon.
    Input: s, length of eash side of the polyton.
    Returns the sum of the area and square of the perimeter 
    of the polygon (rouded to 4 decimal places)
    """

    area = 0.25*n*s**2
    area /= math.tan(math.pi/n)
    perim = n*s
    
    return round(area + perim**2, 4)
