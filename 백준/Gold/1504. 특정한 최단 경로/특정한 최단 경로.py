import sys
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
dp = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][i] = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    dp[a][b] = c
    dp[b][a] = c
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

v1, v2 = map(int, input().split())

answer = min(dp[1][v1] + dp[v1][v2] + dp[v2][n],
             dp[1][v2] + dp[v2][v1] + dp[v1][n],
             )

if answer >= INF:
    answer = -1

print(answer)