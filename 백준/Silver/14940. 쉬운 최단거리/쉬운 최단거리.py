import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

arr = list()
wall = set()

for _ in range(n):
    arr.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(m):
        elt = arr[i][j]
        
        if elt == 2:
            start = (i, j)
        
        if elt == 0:
            wall.add((i, j))
            
def bfs(start):
    visited = [[False for _ in range(m)] for _ in range(n)]
    answer = [[-1 for _ in range(m)] for _ in range(n)]
    
    for r, c in wall:
        answer[r][c] = 0
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    r, c = start[0], start[1]
    
    visited[r][c] = True
    
    queue = deque([[r, c, 0]])
    
    while queue:
        r, c, cnt = queue.popleft()
        
        answer[r][c] = cnt
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            if (0 <= nr < n and 0<= nc < m) and not visited[nr][nc] and (nr, nc) not in wall:
                queue.append((nr, nc, cnt+1))
                visited[nr][nc] = True
                
    return answer

answer_list = bfs(start)

for row in answer_list:
    for elt in row:
        print(elt, end=' ')
    print()