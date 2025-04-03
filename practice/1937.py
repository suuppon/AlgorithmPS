import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

arr = list()
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

dp = [[-1 for _ in range(n)] for _ in range(n)]

def dfs(x, y):
    if dp[y][x] != -1:
        return dp[y][x]
    
    dp[y][x] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        
        if arr[ny][nx] > arr[y][x]:
            dp[y][x] = max(dp[y][x], dfs(nx, ny) + 1)
    
    return dp[y][x]


answer = 0

for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))
    
print(answer)