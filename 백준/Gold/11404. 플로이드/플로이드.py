import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

dp = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    dp[a][b] = min(dp[a][b], c)


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        elt = dp[i][j] if dp[i][j] != INF else 0
        print(elt, end=' ')
    print()