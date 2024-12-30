
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def Combination(n, k):
    if k > n-k:
        k = n-k
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= n-i
        denominator *= i+1
    answer = numerator//denominator

    return answer

n, k = map(int, input().split())

answer = Combination(n, k) % 1_000_000_007

print(answer)