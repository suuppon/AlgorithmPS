from collections import deque
import copy


m, n = map(int, input().split())
table = list()
for _ in range(n):
    row = list(map(int, input().split()))
    table.append(row)

visited = copy.deepcopy(table)

def index_filter(idx):
    x, y = idx[0], idx[1]
    if x >= 0 and x < m and y >= 0 and y < n:
        return True
    return False

def bfs():
    queue = deque()
    for i in range(m):
        for j in range(n):
            if table[j][i] == 1:
                queue.append([(i, j), 0])
                table[j][i] = 0
    maximum = 0
    while queue:
        elt = queue.popleft()
        x, y = elt[0][0], elt[0][1]
        if table[y][x] == 0:
            level = elt[1]
            maximum = max(level, maximum)
            table[y][x] = 1
            tmp_idx = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for idx in filter(index_filter, tmp_idx):
                queue.append([idx, level+1])
                
    return maximum

result = bfs()
        
        
def test():
    for i in range(m):
        for j in range(n):
            if table[j][i] == 0:
                return -1
    return result

print(test())