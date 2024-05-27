import sys
input = sys.stdin.readline


def Binomial(N, K):
    if K > N - K:
        K = N - K

    numerator = 1
    denominator = 1
    for i in range(K):
        numerator = numerator * (N-i)
        denominator = denominator * (i+1)
    
    NCK = numerator//denominator

    return NCK

N, K = map(int, input().split())

answer = Binomial(N, K) % 10007

print(answer)
