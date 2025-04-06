import sys
input = sys.stdin.readline

from collections import deque

def bfs(bridge, cost, departure, arrival, n):
    visited = [False for _ in range(n+1)]
    
    queue = deque(bridge[departure])
    while queue:
        elt = queue.popleft()
        if elt[1] >= cost:
            if elt[0] == arrival:
                return True
            else:
                if not visited[elt[0]]:
                    visited[elt[0]] = True
                    for item in bridge[elt[0]]:
                        queue.append(item)
                        
    return False
                

n, m = map(int, input().split())

bridge = [[] for _ in range(n+1)]


min_cost = 10 ** 10
max_cost = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    bridge[b].append((a, c))
    bridge[a].append((b, c))
    
    max_cost = max(c, max_cost)
    min_cost = min(c, min_cost)
    
num1, num2 = map(int, input().split())

start, end = min_cost, max_cost

answer = 0

while start <= end:
    mid = (start + end) // 2
    
    if bfs(bridge, mid, num1, num2, n):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(answer)