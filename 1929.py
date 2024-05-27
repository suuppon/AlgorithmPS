#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 14:48:19 2023

@author: SAMSUNG
"""
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B_1 = B

B_1.sort(reverse = True)
A.sort()

mult_list = [A[i] * B_1[i] for i in range(len(A))]
print(sum(mult_list)) 
'''import numpy as np

for _ in range(5):
    
    B_1 = B.drop(np.argmax(B))'''

 
            