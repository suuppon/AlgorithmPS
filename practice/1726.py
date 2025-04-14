import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())

Map = list()

for _ in range(M):
    row = list(map(int, input().split()))
    Map.append(row)
    
direction_dir = {1: [0, 1], 2: [0, -1], 3: [1, 0], 4: [-1, 0]}

visited = [[False for _ in range(N)] for _ in range(M)]

def cal_rotation_cost(start_dir, end_dir):
    if set([start_dir, end_dir]) == set([1, 2]) or set([start_dir, end_dir]) == set([3, 4]):
        return 2
    elif start_dir == end_dir:
        return 0
    else:
        return 1

def bfs(start, cur_dir, target):
    table = [[int(1e10) for _ in range(N)] for _ in range(M)]
    
    visited[start[0]][start[1]] = True
    table[start[0]][start[1]] = 0
    
    queue = deque([(start, cur_dir)])
    
    while queue:
        start, cur_dir = queue.popleft()
        r, c = start
        
        if (r, c) == target:
            return table[r][c], cur_dir
        
        for i in [1, 2, 3, 4]:
            dr, dc = direction_dir[i]
            nr, nc = r + dr, c + dc
            if not (0 <= nr < M and 0 <= nc < N):
                continue
            
            if Map[nr][nc] == 0 and not visited[nr][nc]:
                visited[nr][nc] = True
                rotation_cost = cal_rotation_cost(cur_dir, i)
                if rotation_cost == 0:
                    table[nr][nc] = min(table[r][c], table[nr][nc])
                else:
                    table[nr][nc] = min(table[r][c] + 1 + rotation_cost, table[nr][nc])
                queue.append([(nr, nc), i])
                

r_0, c_0, cur_dir = map(int, input().split())
r_t, c_t, target_dir = map(int, input().split())

num_cmd, final_dir = bfs((r_0-1, c_0-1), cur_dir, (r_t-1, c_t-1))
if num_cmd == 0:
    num_cmd = 1
num_cmd += cal_rotation_cost(final_dir, target_dir)

    
print(num_cmd)