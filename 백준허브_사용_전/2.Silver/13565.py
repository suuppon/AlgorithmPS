import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())
table = list()
for _ in range(m):

    row = input()
    table.append(list(row))

def dfs(x ,y):
    global table
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    if table[y][x] == '0':
        table[y][x] = 2
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return False
    return False

def test():
    for i in range(n):
        dfs(i, 0)
    
    for i in range(n):
        if table[m-1][i] == 2:
            return 'YES'
    return 'NO'

result = test()
print(result)