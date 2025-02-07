import sys
input = sys.stdin.readline

from itertools import combinations
from collections import deque
from copy import deepcopy

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

zero_positions = [(r, c) for r in range(m) for c in range(n) if graph[c][r] == 0]

comb = list(combinations(zero_positions, 3))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def contamination(x, y, graph, visited):
    if graph[y][x] != 0:
        visited[y][x] = True
        
    if graph[y][x] == 2:
        queue = deque([(x, y)])
        while queue:
            x, y = queue.popleft()
            graph[y][x] = 2
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0 and not visited[ny][nx]:
                    queue.append((nx, ny))
                    visited[ny][nx] = True
            else:
                continue

max_count = 0

for c in comb:
    graph_copy = deepcopy(graph)
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    for point in c:
        graph_copy[point[1]][point[0]] = 1
    
    for i in range(m):
        for j in range(n):
            contamination(i, j, graph_copy, visited)
                
    count = 0
    for i in range(m):
        for j in range(n):
            if graph_copy[j][i] == 0:
                count += 1

    max_count = max(max_count, count)
        
print(max_count)