#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:54:59 2023

@author: SAMSUNG
"""
from collections import Counter

N = int(input())
a = list()
for _ in range(N):
    x = int(input())
    a.append(x)
    
a.sort()

mean = round(sum(a)/len(a))

median = a[int(N//2)]

if N == 1:
    mode = x
else:
    cnt = Counter(a)
    m_list = cnt.most_common(2)
    if m_list[0][0]>m_list[1][0]:
        mode = m_list[0][0]
    else:
        mode = m_list[1][0]

interval = a[-1]-a[0]

    
    
    
print(mean)
print(median)
print(mode)
print(interval)
