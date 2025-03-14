import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())

dp = [[INF for _ in range(v+1)] for _ in range(v+1)]

for i in range(1, v+1):
    dp[i][i] = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    dp[a][b] = c
    
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            dp[i][j] = min(dp[i][k] + dp[k][j], dp[i][j])

answer = INF

for i in range(1, v+1):
    for j in range(1, v+1):
        if i != j:
            answer = min(answer, dp[i][j] + dp[j][i])

if answer >= INF:
    answer = -1

print(answer)