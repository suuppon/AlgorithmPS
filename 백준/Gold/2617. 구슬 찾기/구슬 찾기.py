import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

heavy_list = [[] for _ in range(n+1)]
light_list = [[] for _ in range(n+1)]

for _ in range(m):
    heavy, light = map(int, input().split())
    heavy_list[light].append(heavy)
    light_list[heavy].append(light)
    
# 자신보다 무거운 게 (N+1) / 2 개 이상이면 cnt += 1

def bfs(start, graph):
    visited = [False for _ in range(n+1)]
    visited[start] = True
    queue = deque([start])
    
    cnt = 0
    while queue:
        num = queue.popleft()
        
        for elt in graph[num]:
            if not visited[elt]:
                cnt += 1
                visited[elt] = True
                queue.append(elt)
                
    return cnt

cnt = 0

for i in range(1, n+1):
    if bfs(i, heavy_list) >= (n+1) // 2 or bfs(i, light_list) >= (n+1) // 2:
        cnt += 1

print(cnt)