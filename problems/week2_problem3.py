#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:04:08 2017

@author: gfpp
"""

import math

#balance = 320000    # Lowest Payment: 29157.09
balance = 999999    # Lowest Payment: 90325.03
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12.0
iniBalance = balance

# Bisection search initial variables
totalInsterest = math.pow((1 + monthlyInterestRate),12)
low = balance / 12.0
high = (balance*totalInsterest) / 12.0
fixedMonthlyPayment = round((high + low)/2.0, 2)

epsilon = 0.10

while True:
    #print("FixedMonthlyPayment:", fixedMonthlyPayment)
    for m in range(1,13):
        monthlyUnpaydBalance = balance - fixedMonthlyPayment
        balance = monthlyUnpaydBalance + monthlyInterestRate*monthlyUnpaydBalance        
        #print("   Month", m, "Remaining balance:", balance)
    
    if abs(balance) < epsilon:
        break
    elif balance > 0:
        balance = iniBalance
        low = fixedMonthlyPayment
    else:
        balance = iniBalance
        high = fixedMonthlyPayment
        
    fixedMonthlyPayment = round((high + low)/2.0, 2)

print("Lowest Payment:", str(round(fixedMonthlyPayment,2)))
