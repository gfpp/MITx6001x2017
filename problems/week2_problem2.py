#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 10:36:33 2017

@author: gfpp
"""

balance = 3329  # fixedMonthlyPayment: 310
#balance = 4773  # fixedMonthlyPayment: 440
#balance = 3926  # fixedMonthlyPayment: 360
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0
fixedMonthlyPayment = 10
iniBalance = balance

while True:
    print("FixedMonthlyPayment:", fixedMonthlyPayment)
    for m in range(1,13):
        monthlyUnpaydBalance = balance - fixedMonthlyPayment
        balance = monthlyUnpaydBalance + monthlyInterestRate*monthlyUnpaydBalance        
        print("   Month", m, "Remaining balance:", str(round(balance,2)))

    if balance < 0:
        break
    else:
        balance = iniBalance
        fixedMonthlyPayment += 10
    
print("Lowest Payment:", str(fixedMonthlyPayment))
