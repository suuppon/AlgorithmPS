from collections import deque

m, n, h = map(int, input().split())
tmp_table = list()
table = list()
for __ in range(h):
    for _ in range(n):
        row = list(map(int, input().split()))
        tmp_table.append(row)
    table.append(tmp_table)


def index_filter(idx):
    x, y, z = idx[0], idx[1], idx[2]
    if x >= 0 and x < m and y >= 0 and y < n and z >= 0 and z < h and table[z][y][x] == 0:
        return True
    return False

def bfs():
    queue = deque()
    for i in range(m):
        for j in range(n):
            for k in range(h):
                if table[k][j][i] == 1:
                    queue.append([(i, j, k), 0])
                    table[k][j][i] = 0
    maximum = 0
    while queue:
        elt = queue.popleft()
        x, y, z = elt[0][0], elt[0][1], elt[0][2]
        if table[z][y][x] == 0:
            level = elt[1]
            maximum = max(level, maximum)
            table[z][y][x] = 1
            tmp_idx = [(x-1, y, z), 
                       (x+1, y, z), 
                       (x, y-1, z), 
                       (x, y+1, z),
                       (x, y, z-1),
                       (x, y, z+1)]
            for idx in filter(index_filter, tmp_idx):
                queue.append([idx, level+1])
                
    return maximum

result = bfs()
        
        
def test():
    for i in range(m):
        for j in range(n):
            for k in range(h):
                if table[k][j][i] == 0:
                    return -1
    return result

print(test())