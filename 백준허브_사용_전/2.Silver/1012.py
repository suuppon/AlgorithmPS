import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())

def test():
    m, n, k = map(int, input().split())
    table = [[0 for _ in range(m)] for __ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        table[y][x] = 1
    
    def dfs(x ,y):
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        
        if table[y][x] == 1:
            table[y][x] = 0
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
        return False
    
    cnt = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j):
                cnt += 1
    
    return cnt
                
for _ in range(T):
    result = test()
    print(result)
    
    
    