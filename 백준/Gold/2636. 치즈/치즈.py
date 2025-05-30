from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())

table = list()

for _ in range(R):
    table.append(list(map(int, input().split())))
    
    
def bfs(rs, cs):
    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[rs][cs] = True
    
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    melt = set()
    
    queue = deque([(rs, cs)])
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            if 0<= nr < R and 0<= nc < C and not visited[nr][nc]:
                visited[nr][nc] = True
                
                if table[nr][nc] == 1:
                    melt.add((nr, nc))
                else:
                    queue.append((nr, nc))

    for r, c in melt:
        table[r][c] = 0
        
    if melt:
        return len(melt)
    else:
        return False
    
cnt = 0

while True:
    answer = bfs(0, 0)
    if answer:
        cnt += 1
        num = answer
    else:
        break
    
print(cnt)
print(num)