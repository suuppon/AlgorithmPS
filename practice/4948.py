import sys
import math

input = sys.stdin.readline

def PrimeCheck(n:int):
    if n == 1:
        return False

    k = 2
    while k <= math.sqrt(n):
        if n % k == 0:
            return False
        else:
            k += 1
    
    return True

num_list = [num for num in range(0, 123456*2 + 1)]

for i in range(len(num_list)):
    num_list[i] = PrimeCheck(num_list[i])

while True:
    n = int(input())

    if n == 0:
        break
    else:
        num_of_prime = sum(num_list[n+1:2*n+1])

    print(num_of_prime)