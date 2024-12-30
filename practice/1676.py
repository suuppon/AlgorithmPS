#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 19:36:53 2023

@author: SAMSUNG
"""
z = 0
n = int(input())



def fac(x):
    if x == 1 or x == 0:
        return 1
    else:
        return fac(x-1) * x

X = str(fac(n))
if n==0 or n==1 or n ==2 or n==3:
    print(0)
for i in range(1,len(X)):
    if X[-i] =='0':
        z += 1
    else:
        print(z)
        break
    
