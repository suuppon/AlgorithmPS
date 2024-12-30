import sys
input = sys.stdin.readline

n, m = map(int, input().split())

paper = list()

for _ in range(n):
    row = list(map(int, input().split()))
    paper.append(row)

visited = [[False] * m for _ in range(n)]

dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

maximum = 0

def case1(x, y, tmp, cnt):
    # Case1. 'ㅜ' 모양을 제외한 케이스.
    global maximum
    
    if cnt == 4:
        maximum = max(tmp, maximum)
        return
    
    for dx, dy in dxdy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
            visited[ny][nx] = True
            case1(nx, ny, tmp + paper[ny][nx], cnt + 1)
            visited[ny][nx] = False
        
def case2(x, y):
    global maximum
    
    left, right, up, down = None, None, None, None
    
    if x == 0:
        left = -9999
    if y == 0:
        up = -9999
    if x == m - 1:
        right = -9999
    if y == n - 1:
        down = -9999
    
    if left == None:
        left = paper[y][x-1]
    if right == None:
        right = paper[y][x+1]
    if up == None:
        up = paper[y-1][x]
    if down == None:
        down = paper[y+1][x]
        
    minimum = min(left, right, up, down)
    maximum = max(maximum, (paper[y][x] + left + right + up + down - minimum))
    
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        case1(i, j, 0, 0)
        visited[i][j] = False
        case2(j, i)
print(maximum)