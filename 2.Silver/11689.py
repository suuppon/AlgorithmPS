import sys
input = sys.stdin.readline

def prime_factor(n):
    factor_set = set()
    factor = 2

    while n >= factor:
        if n%factor == 0:
            factor_set.add(factor)
            n = n//factor
            factor += 1
        else:
            factor += 1
    return factor_set

n = int(input())


c = 1
for i in range(2, n):
    if len(prime_factor(i).intersection(prime_factor(n))) == 0:
        c += 1

print(c)