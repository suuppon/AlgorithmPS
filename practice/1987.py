import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

r, c = map(int, input().split())

graph = list()

for _ in range(r):
    row = list(input())
    graph.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count, visited_set):
    global max_count
    max_count = max(max_count, count)
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < c and 0 <= ny < r and graph[ny][nx] not in visited_set:
            dfs(nx, ny, count+1, visited_set | {graph[ny][nx]})

visited_set = {graph[0][0]}
max_count = 0
dfs(0, 0, 1, visited_set)

print(max_count)