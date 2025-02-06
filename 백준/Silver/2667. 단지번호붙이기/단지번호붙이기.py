import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())

table = list()

for _ in range(n):

    row = list(input())
    table.append(row)
    
def dfs(x, y, count):
    if x >= n or x < 0 or y >= n or y < 0:
        return count
    if table[y][x] == '0':
        return count

    count += 1
    table[y][x] = '0'
    
    count = dfs(x-1, y, count)
    count = dfs(x, y-1, count)
    count = dfs(x+1, y, count)
    count = dfs(x, y+1, count)
    
    return count

c_list = list()
n_group = 0

for i in range(n):
    for j in range(n):
        count = dfs(i, j, 0)
        if count != 0:
            n_group += 1
            c_list.append(count)

print(n_group)
c_list.sort()
for c in c_list:
    print(c)