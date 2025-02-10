import copy
import sys

input = sys.stdin.readline

m, n = map(int, input().split())

Map = list(list(map(int, input().split())) for _ in range(m))

count = 0

def dfs(x, y, visited):
    global count
    
    visited[y][x] = True
    if visited[m-1][n-1] == True:
        count += 1
        return None
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and Map[ny][nx] < Map[y][x] and not visited[ny][nx]:
            visited_copy = copy.deepcopy(visited)
            dfs(nx, ny, visited_copy)

visited = [[False for _ in range(n)] for _ in range(m)]
            
visited[0][0] = True

dfs(0, 0, visited)
print(count)