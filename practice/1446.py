import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, d = map(int, input().split())

graph = [[] for _ in range(d+1)]

for _ in range(n):
    start, end, dist = map(int, input().split())
    if end <= d:
        graph[start].append((dist, end))
    
for i in range(1, d+1):
    graph[i-1].append((1, i))
    
distance = [INF for _ in range(d+1)]

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        
        if dist > distance[now]:
            continue
        
        for additional_cost, end in graph[now]:
            cost = dist + additional_cost
            if cost < distance[end]:
                distance[end] = cost
                heapq.heappush(queue, (cost, end))

dijkstra(0)
print(distance[d])