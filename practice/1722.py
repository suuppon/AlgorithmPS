import sys
input = sys.stdin.readline
import math
from math import factorial as f

N = int(input())
arr = list(range(1, N+1))

q = list(map(int, input().split()))

k = q[0]
target = q[1:]

answer = []

# case 1. k == 1
if k == 1:
    target = q[0]
    length = N-1
    index = 0
    for i in range(N):
        factorial = f(length)
        idx = target // factorial
        answer.append(arr[idx])
        
        target -= factorial
        arr.remove(arr[idx])
        length -= 1
print(answer)

# case 2. k == 2
if k == 2:
    for i in range(len(comb)):
        if tuple(target) == comb[i]:
            answer = i+1
            break
    
    print(answer)