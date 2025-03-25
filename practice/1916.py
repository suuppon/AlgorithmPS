import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

n, m = int(input()), int(input())

graph = [list() for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
def dijkstra(start, end):
    distance = [INF for _ in range(n+1)]
    distance[start] = 0
    
    queue = [(0, start)]
    heapq.heapify(queue)
    
    while queue:
        dist, cur = heapq.heappop(queue)
        
        if distance[cur] < dist:
            continue
        
        for dest, additionalCost in graph[cur]:
            cost = dist + additionalCost
            if cost < distance[dest]:
                distance[dest] = cost
                heapq.heappush(queue, (cost, dest))
        
    return distance[end]

start, end = map(int, input().split())

print(dijkstra(start, end))