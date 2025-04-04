import sys
input = sys.stdin.readline

num_list = list()
T, W = map(int, input().split())

for _ in range(T):
    num_list.append(int(input()))
    
dp = [[0 for _ in range(W+1)] for _ in range(T+1)]

dp[1][0] = num_list[1] % 2
dp[1][1] = num_list[1] // 2

for t in range(2, T+1):
    for w in range(W+1):
        