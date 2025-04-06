import sys
input = sys.stdin.readline
INF = int(1e9)
import heapq

V, E = map(int, input().split())
K = int(input())

graph = [list() for _ in range(V+1)]


for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

def dijkstra(start):
    distance = [INF for _ in range(V+1)]
    distance[start] = 0
    
    queue = [(0, start)]
    heapq.heapify(queue)
    
    visited = [False for _ in range(V+1)]
    visited[start] = True
    while queue:
        dist, curNode = heapq.heappop(queue)
        if dist > distance[curNode]:
            continue
        
        for additionalDist, neighbor in graph[curNode]:
            cost = dist + additionalDist
            if cost < distance[neighbor]:
                distance[neighbor] = cost
                heapq.heappush(queue, (cost, neighbor))
    
    return distance

distance = dijkstra(K)
for i in range(1, V+1):
    elt = distance[i] if distance[i] != INF else 'INF'
    print(elt)