from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])

check = [0] * (n+1)
def bfs():
    while queue:
        elt = queue.popleft()
        for nxt in graph[elt]:
            if not check[nxt]:
                check[nxt] = elt
                queue.append(nxt)
            
        
bfs()
res = check[2:]
for ans in res:
    print(ans)