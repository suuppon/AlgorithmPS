import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def Combination(n, k):
    if k > n-k:
        k = n-k

    value = 1

    for i in range(k):
        value *= (n-i)/(i+1)
    
    return int(value)

print(Combination(n, k))