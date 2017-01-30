#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 10:15:23 2017

@author: gfpp
"""

balance = 484
annualInterestRate = 0.20
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12.0

for m in range(1,13):
    minMonthlyPayment = monthlyPaymentRate*balance
    monthlyUnpaydBalance = balance - minMonthlyPayment
    balance = monthlyUnpaydBalance + monthlyInterestRate*monthlyUnpaydBalance
    print("Month", m, "Remaining balance:", str(round(balance,2)))
    

print("Remaining balance:" + str(round(balance,2)))