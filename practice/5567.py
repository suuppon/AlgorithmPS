import sys
input = sys.stdin.readline
from collections import deque

n, m = int(input()), int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(start):
    queue = deque([(0, start)]) #(cnt, start)
    
    visited = [False for _ in range(n+1)]
    visited[start] = True
    num = -1
    while queue:
        cnt, curNode = queue.popleft()
        if cnt == 3:
            break
        
        num += 1
        
        for neighbor in graph[curNode]:
            if not visited[neighbor]:
                queue.append((cnt+1, neighbor))
                visited[neighbor] = True
    
    return num

print(bfs(1))