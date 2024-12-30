#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 13:39:38 2023

@author: SAMSUNG
"""

P = [1,1,1,2,2]

T = int(input())
for j in range(100):
        P.append(P[-1]+P[-5])
        
for _ in range(T):
    n = int(input())
    print(P[n-1])