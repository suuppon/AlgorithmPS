import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]
distance[0] = -INF
for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append((1, n2))
    graph[n2].append((1, n1))

visited = [False for _ in range(n+1)]

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        
        if dist > distance[now]:
            continue
        
        for additional_cost, dest in graph[now]:
            cost = dist + additional_cost
            if cost < distance[dest]:
                distance[dest] = cost
                heapq.heappush(queue, (cost, dest))

dijkstra(1)

target_num = 0
maximum = max(distance)
cnt = 0
for i in range(1, n+1):
    if distance[i] == maximum:
        cnt += 1
        if not target_num:
            target_num = i
            
print(target_num, maximum, cnt)