import sys
input = sys.stdin.readline
import math
from math import factorial as f

N = int(input())
arr = list(range(1, N+1))

q = list(map(int, input().split()))

k = q[0]
target = q[1:]
length = N-1

# case 1. k == 1
if k == 1:
    answer = []
    target = q[1]
    index = 0
    for i in range(N):
        factorial = f(length)
        
        idx = (target-1) // factorial
        answer.append(arr[idx])
        
        if idx != 0:
            target %= factorial
        arr.remove(arr[idx])
        length -= 1
    for elt in answer:
        print(elt, end=' ')

# case 2. k == 2
if k == 2:
    answer = 1
    for i in range(N):
        num = target[i]
        
        for j in range(len(arr)):
            if arr[j] == num:
                idx = j
                break
        
        factorial = f(length)
        answer += idx * factorial
        
        length -= 1
        arr.remove(num)
    
    print(answer)