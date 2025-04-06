import math

T = int(input())

for i in range(T):
    n,m = input().split()
    n = int(n)
    m = int(m)
    print(math.comb(m,n))