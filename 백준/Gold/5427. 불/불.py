import sys
input = sys.stdin.readline
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_outside(r, c):
    return not (0 <= r < h and 0 <= c < w)

def bfs_fire(fire_list):
    arr = [[-1 for _ in range(w)] for _ in range(h)]
    queue = deque()
    for r, c in fire_list:
        arr[r][c] = 0
        queue.append((r, c, 0))
        
    while queue:
        r, c, cnt = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not is_outside(nr, nc):
                if Map[nr][nc] in ('.', '@') and arr[nr][nc] == -1:
                    arr[nr][nc] = cnt + 1
                    queue.append((nr, nc, cnt+1))
    return arr

def bfs(sr, sc, fire_map):
    queue = deque()
    queue.append((sr, sc, 0))
    
    visited = [[False for _ in range(w)] for _ in range(h)]
    visited[sr][sc] = True

    while queue:
        r, c, cnt = queue.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if is_outside(nr, nc):
                return cnt + 1
            if 0 <= nr < h and 0 <= nc < w:
                if not visited[nr][nc] and Map[nr][nc] != '#':
                    if fire_map[nr][nc] == -1 or fire_map[nr][nc] > cnt + 1:
                        visited[nr][nc] = True
                        queue.append((nr, nc, cnt+1))
    return 'IMPOSSIBLE'

T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    Map = [list(input().strip()) for _ in range(h)]
    
    fire_list = []
    for i in range(h):
        for j in range(w):
            if Map[i][j] == '*':
                fire_list.append((i, j))
            elif Map[i][j] == '@':
                sr, sc = i, j

    fire_map = bfs_fire(fire_list)
    print(bfs(sr, sc, fire_map))