import sys
sys.setrecursionlimit(10**6)

# n : 행 개수, m : 열 개수
n, m = map(int, input().split())

paper = list()

for _ in range(n):
    paper.append(list(map(int, input().split())))

visited = [[False for _ in range(m)] for _ in range(n)]
cnt = 0
maximum = 0

def dfs(x, y, visited, size):
    if x < 0 or x >= m or y < 0 or y >= n or visited[y][x]:
        return size
    
    visited[y][x] = True
    if paper[y][x] == 1:
        size += 1
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            size = dfs(nx, ny, visited, size)
        
        return size
    else:
        return size
    
for i in range(n):
    for j in range(m):
        size = dfs(j, i, visited, 0)
        if size:
            cnt += 1
        maximum = max(size, maximum)

print(cnt)
print(maximum)
