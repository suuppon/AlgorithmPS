from collections import deque

n, m = map(int, input().split())

graph = list()

for _ in range(n):
    row = input()
    graph.append(list(row))
    
start = (0, 0)
visited = [[0 for _ in range(m)] for __ in range(n)]
queue = deque([[start, 1]])

def filter_idx(i):
    if i[0] < 0 or i[0] > m-1 or i[1] < 0 or i[1] > n-1 or visited[i[1]][i[0]] == 1:
        return False
    return True

while True:
    elt = queue.popleft()
    x, y = elt[0][0], elt[0][1]
    level = elt[1] 
    
    if x == m-1 and y == n-1:
        print(level)
        break
    
    if graph[y][x] == '1' and not visited[y][x]:
        visited[y][x] = 1
        for idx in filter(filter_idx, [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]):
            queue.append([idx, level+1])
        