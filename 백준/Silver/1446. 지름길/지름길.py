import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, d = map(int, input().split())

graph = [[] for _ in range(d+1)]

for _ in range(n):
    start, end, length = map(int, input().split())
    if end <= d:
        graph[start].append((end, length))
    
for i in range(1, d+1):
    graph[i-1].append((i, 1))
    
distance = [INF for _ in range(d+1)]

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        
        if dist > distance[now]:
            continue
        
        for item in graph[now]:
            cost = dist + item[1]
            if cost < distance[item[0]]:
                distance[item[0]] = cost
                heapq.heappush(queue, (cost, item[0]))

dijkstra(0)
print(distance[d])