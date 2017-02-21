#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 11:44:31 2017

@author: gfpp
"""

# x is prime if (x % p) != 0 for all earlier primes p.
def genPrimes():
    prime = [2]
    x = 2
    yield x
    while True:
        isPrime = True
        x += 1
        for p in prime:
            isPrime = isPrime and (x % p) != 0
        if isPrime:
            prime.append(x)
            yield x
        