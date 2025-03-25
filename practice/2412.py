import sys
input = sys.stdin.readline
from collections import deque

n, T = map(int, input().split())

point_list = set()

for _ in range(n):
    x, y = map(int, input().split())
    point_list.add((x, y))

def bfs():
    visited = set()
    queue = deque([(0, (0, 0))]) # (count, (x, y))
    answer = -1
    
    while queue:
        cnt, (x, y) = queue.popleft()
        if y == T:
            answer = cnt
            break
        
        for i in range(-2, 3):
            for j in range(-2, 3):
                nx = x + i
                ny = y + j
                if (nx, ny) in point_list and (nx, ny) not in visited:
                    queue.append((cnt+1, (nx, ny)))
                    visited.add((nx, ny))
    
    return answer

print(bfs())