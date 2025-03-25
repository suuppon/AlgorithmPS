import sys
input = sys.stdin.readline
INF = int(1e9)
import heapq
from collections import defaultdict, deque

def dijkstra(start, end):
        
    distance = [INF for _ in range(n)]
    distance[start] = 0
    
    queue = [(0, start)]
    heapq.heapify(queue)
    while queue:
        dist, cur = heapq.heappop(queue)
        
        if dist > distance[cur]:
            continue
        
        for dest, additionalDist in graph[cur]:
            cost = additionalDist + dist
            
            if cost < distance[dest]:
                parents[dest].append(cur)
                distance[dest] = cost
                heapq.heappush(queue, (cost, dest))
                
    return distance[end]

def remove_shortest_paths(end):
    queue = deque([end])
    while queue:
        cur = queue.popleft()
        if cur == start:
            continue
        for prev in parents[cur]:
            if (prev, cur) in edge_set:
                edge_set.remove((prev, cur))
                queue.append(prev)

while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    
    start, end = map(int, input().split())
    
    graph = defaultdict(list)
    edge_set = set()
    parents = defaultdict(list)
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        edge_set.add((a, b))
        
    optimal = dijkstra(start, end)
    
    remove_shortest_paths(end)
    
    graph = {u: [(v, p) for v, p in graph[u] if (u, v) in edge_set] for u in graph}
    parent = defaultdict(list)
    suboptimal = dijkstra(start, end)
    answer = suboptimal
    
    if answer >= INF:
        answer = -1
    
    print(answer)