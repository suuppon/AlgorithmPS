import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    dp[a][b] = 1
    dp[b][a] = 1
    
for i in range(1, n+1):
    for j in range(1, n+1):
        if i != j and dp[i][j] == 0:
            dp[i][j] = INF

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b])

bacon_num_list = [sum(row) for row in dp]
bacon_num_list[0] = INF
minimum = min(bacon_num_list)

for i in range(1, n+1):
    if bacon_num_list[i] == minimum:
        answer = i
        break
print(i)