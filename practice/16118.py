import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

n, m = map(int, input().split())

graph = [list() for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra_adjusted(start):
    distance = [INF for _ in range(n+1)]
    distance[start] = 0
    
    cnt = 0
    queue = [(0, start, cnt)]
    heapq.heapify(queue)
    
    while queue:
        dist, cur, cnt = heapq.heappop(queue)
        
        if distance[cur] < dist:
            continue
        
        for dest, additional_cost in graph[cur]:
            if cnt % 2 == 0:
                additional_cost /= 2
            else:
                additional_cost *= 2
            
            cost = dist + additional_cost
            if cost < distance[dest]:
                distance[dest] = cost
                heapq.heappush(queue, (cost, dest, cnt+1))
                
    return distance
                
def dijkstra(start):
    distance = [INF for _ in range(n+1)]
    distance[start] = 0
    
    queue = [(0, start)]
    heapq.heapify(queue)
    
    while queue:
        dist, cur = heapq.heappop(queue)
        
        if distance[cur] < dist:
            continue
        
        for dest, additional_cost in graph[cur]:
            cost = dist + additional_cost
            if cost < distance[dest]:
                distance[dest] = cost
                heapq.heappush(queue, (cost, dest))
    
    return distance

fox = dijkstra(1)
wolf = dijkstra_adjusted(1)

cnt = 0
for i in range(2, n+1):
    if fox[i] < wolf[i]:
        cnt += 1

print(cnt)