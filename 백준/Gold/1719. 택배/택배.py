import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [list() for _ in range(n+1)]
dp = [[INF for _ in range(n+1)] for _ in range(n+1)]

answer_list = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    dp[a][b] = c
    dp[b][a] = c
    
    answer_list[a][b] = b
    answer_list[b][a] = a
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            cost_old = dp[i][j]
            cost_new = dp[i][k] + dp[k][j]
            
            if cost_old > cost_new:
                dp[i][j] = cost_new
                answer_list[i][j] = answer_list[i][k]

for i in range(1, n+1):
    for j in range(1, n+1):
        elt = answer_list[i][j] if answer_list[i][j] != 0 else '-'
        print(elt, end=' ')
    print()