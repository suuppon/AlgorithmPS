import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())

graph = list()

for _ in range(M):
    row = list(map(int, input().split()))
    graph.append(row)
    
sr, sc, sd = map(int, input().split())
tr, tc, td = map(int, input().split())

list_dr = [None, 0, 0, 1, -1]
list_dc = [None, 1, -1, 0, 0]

def cal_rotation_cost(d1, d2):
    if {d1, d2} == {1, 2} or {d1, d2} == {3, 4}:
        return 2
    elif d1 == d2:
        return 0
    else:
        return 1

def bfs(sr, sc, sd, tr, tc, td):
    queue = deque([(sr, sc, sd, 0)])
    visited = [[set() for _ in range(N)] for _ in range(M)]
    
    while queue:
        r, c, d, cnt = queue.popleft()
        
        if (r, c, d) == (tr, tc, td):
            return cnt
        
        for l in range(1, 4):
            nr, nc = r + list_dr[d] * l, c + list_dc[d] * l
            nd = d
            if not (0 <= nr < M and 0 <= nc < N):
                break
            if graph[nr][nc] == 1:
                break
            if nd in visited[nr][nc]:
                continue
            queue.append((nr, nc, nd, cnt+1))
            visited[nr][nc].add(nd)
            
        for nd in [1, 2, 3, 4]:
            if nd not in visited[r][c]:
                rotation_cost = cal_rotation_cost(d, nd)
                queue.append((r, c, nd, cnt+rotation_cost))
                visited[r][c].add(nd)
                
answer = bfs(sr-1, sc-1, sd, tr-1, tc-1, td)
print(answer)