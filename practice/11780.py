import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = int(input()), int(input())

dp = [[INF for _ in range(n+1)] for _ in range(n+1)]
path_list = [[list() for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    dp[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    
    dp[a][b] = min(dp[a][b], c)
    
    path_list[a][b] = [a, b]
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            old_cost = dp[i][j]
            new_cost = dp[i][k] + dp[k][j]
            
            if new_cost < old_cost:
                # path_list update algorithm. 여기가 핵심
                path_list[i][j] = path_list[i][k] + path_list[k][j][1:]
                dp[i][j] = new_cost
                

for i in range(1, n+1):
    for j in range(1, n+1):
        elt = dp[i][j] if dp[i][j] != INF else 0
        print(elt, end=' ')
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        print(len(path_list[i][j]), end=' ')
        for elt in path_list[i][j]:
            print(elt, end=' ')
        print()