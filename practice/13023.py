import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(start, visited, cnt):
    global answer 

    if cnt == 4:
        answer = 1
        return 

    visited[start] = True
    
    for node in graph[start]:
        if not visited[node]:
            dfs(node, visited, cnt+1)
    
    visited[start] = False

for i in range(n):
    answer = 0
    visited = [False for _ in range(n)]
    dfs(i, visited, 0)
    if answer == 1:
        break
    
print(answer)