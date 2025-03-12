import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

n, m = map(int, input().split())

# graph의 의미 : a에서 b로 가려면 cost만큼 든다 -> (cost, b) is in graph[a]
graph = [list() for _ in range(n+1)]

distance = [INF for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
    
def dijkstra(start):
    queue = list()
    queue.append((0, start))
    heapq.heapify(queue)
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

print(distance[n])