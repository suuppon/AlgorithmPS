import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())

arr = list()

for _ in range(R):
    row = list(input().rstrip())
    arr.append(row)

water_loc = list()
water_expanding = list()
wall_loc = list()
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'D':
            rt, ct = i, j
        elif arr[i][j] == '*':
            water_loc.append((i, j))
            water_expanding.append((i, j))
        elif arr[i][j] == 'S':
            rs, cs = i, j
        elif arr[i][j] == 'X':
            wall_loc.append((i, j))

def valid_idx(r, c):
    if 0<=r<R and 0<=c<C:
        return True
    else:
        return False

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(rs, cs):
    global water_table
    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[rs][cs] = True
    queue = deque([(rs, cs, 0)])
    
    while queue:
        r, c, cnt = queue.popleft()
        
        if (r, c) == (rt, ct):
            return cnt
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if valid_idx(nr, nc) and not visited[nr][nc] and (nr, nc) not in wall_loc and (
                cnt+1 < water_table[nr][nc] or water_table[nr][nc] == -1):
                visited[nr][nc] = True
                queue.append((nr, nc, cnt+1))
        
        
    return 'KAKTUS'

water_table = [[-1 for _ in range(C)] for _ in range(R)]

def bfs_water(water_loc):
    visited = [[False for _ in range(C)] for _ in range(R)]
    queue = deque()
    for r, c in water_loc:
        queue.append((r, c, 0))
        water_table[r][c] = 0
        visited[r][c] = True
        
    while queue:
        r, c, cnt = queue.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if valid_idx(nr, nc) and (nr, nc) not in wall_loc and not visited[nr][nc] and arr[nr][nc] not in ('D', 'X'):
                visited[nr][nc] = True
                water_table[nr][nc] = cnt+1
                queue.append((nr, nc, cnt+1))
            
    return water_table

water_table = bfs_water(water_loc)
print(bfs(rs, cs))