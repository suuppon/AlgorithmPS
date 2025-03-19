import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = int(input()), int(input())
dp = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][i] = 0

for _ in range(m):
    h, l = map(int, input().split())
    dp[h][l] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for i in range(1, n+1):
    cnt_row = 0
    for j in range(1, n+1):
        if (dp[i][j], dp[j][i]) == (INF, INF):
            cnt_row +=1
    print(cnt_row)