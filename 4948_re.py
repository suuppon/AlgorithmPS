import math
import sys
input = sys.stdin.readline

def PrimeCheck(n):
    if n == 1:
        return False
    if n == 2:
        return True
    
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    
    else:
        return True
    
prime_list = list()

for num in range(1, 123456*2+100):
    if PrimeCheck(num):
        prime_list.append(num)
while True:
    n = int(input())
    if n == 0:
        break

    c = 0
    i = 0
    while prime_list[i] <= 2*n:
        if prime_list[i] <= n:
            i += 1
        elif n < prime_list[i]:
            c += 1
            i += 1
    print(c)
