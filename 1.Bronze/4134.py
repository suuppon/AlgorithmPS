import sys
import math

input = sys.stdin.readline

def PrimeCheck(n:int):
    k = 2
    while k <= math.sqrt(n):
        if n % k == 0:
            return False
        else:
            k += 1
    
    return True

n = int(input())

for _ in range(n):
    x = int(input())
    c = 0
    while True:
        if x ==0 or x == 1:
            x = 1 
            c = 1
            break
        elif PrimeCheck(x+c) == True:
            break
        else:
            c += 1
    print(x+c)