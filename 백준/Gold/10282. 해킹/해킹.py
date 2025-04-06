import sys
input = sys.stdin.readline
INF = int(1e9)
import heapq

def dijkstra(start, graph):
    distance = [INF for _ in range(n+1)]
    distance[start] = 0
    cntElt = 0
    maxDist = 0
    
    queue = [(0, start)]
    heapq.heapify(queue)
    
    while queue:
        dist, cur = heapq.heappop(queue)
        
        if distance[cur] < dist:
            continue
        
        for dest, additionalDist in graph[cur]:
            cost = dist + additionalDist
            if cost < distance[dest]:
                distance[dest] = cost
                heapq.heappush(queue, (cost, dest))
    
    for d in distance:
        if d < INF:
            cntElt += 1
            maxDist = max(maxDist, d)
                
    return cntElt, maxDist

T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    
    graph = [list() for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
        
    num, time = dijkstra(c, graph)
    print(num, time)
