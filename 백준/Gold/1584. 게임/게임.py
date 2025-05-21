from collections import deque

table = [[0 for _ in range(501)] for _ in range(501)]

N = int(input())

for _ in range(N):
    X1, Y1, X2, Y2 = map(int, input().split())
    minX, maxX = min(X1, X2), max(X1, X2)
    minY, maxY = min(Y1, Y2), max(Y1, Y2)
    for x in range(minX, maxX+1):
        for y in range(minY, maxY+1):
            table[y][x] = 1
            
M = int(input())

for _ in range(M):
    X1, Y1, X2, Y2 = map(int, input().split())
    minX, maxX = min(X1, X2), max(X1, X2)
    minY, maxY = min(Y1, Y2), max(Y1, Y2)
    for x in range(minX, maxX+1):
        for y in range(minY, maxY+1):
            table[y][x] = -1
            
table[0][0] = 0

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[False for _ in range(501)] for _ in range(501)]
    
    queue = deque([(x, y, 0)])
    visited[y][x] = True
    
    while queue:
        x, y, cost = queue.popleft()
        
        if (x, y) == (500, 500):
            return cost
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx <= 500 and 0 <= ny <= 500 and not visited[ny][nx] and table[ny][nx] != -1:
                visited[ny][nx] = True
                if table[ny][nx] == 1:
                    queue.append((nx, ny, cost+1))
                else:
                    queue.appendleft((nx, ny, cost))
                    
    return -1

print(bfs(0, 0))