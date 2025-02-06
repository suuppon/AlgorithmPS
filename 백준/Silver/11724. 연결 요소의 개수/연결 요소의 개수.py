import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

visited = [0 for _ in range(n+1)]
graph = list([] for _ in range(n+1))

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    visited[start] = 1
    queue = deque([start])
    while queue:
        elt = queue.popleft()
        for neighbor in graph[elt]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                queue.append(neighbor)

cnt = 0

for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        bfs(i)
        
print(cnt)