import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n, m = map(int, input().split())

def count_elements(array, visited):
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                if dfs(array, j, i, visited):
                    cnt += 1
    
    return cnt
                    
def dfs(arr, x, y, visited):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    
    if arr[y][x] and not visited[y][x]:
        visited[y][x] = True
        dfs(arr, x-1, y, visited)
        dfs(arr, x, y-1, visited)
        dfs(arr, x+1, y, visited)
        dfs(arr, x, y+1, visited)
        return True
    elif not visited[y][x]:
        visited[y][x] = True
        
        return False

    else:
        return False

def melt(array):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    tmp_array = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(m):
        for j in range(n):
            if array[j][i] != 0:
                zero_cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    else:
                        if array[ny][nx] == 0:
                            zero_cnt += 1
            
                tmp_array[j][i] = zero_cnt
    
    for i in range(m):
        for j in range(n):
            array[j][i] = max(array[j][i] - tmp_array[j][i], 0)
    
    return array
        

def main():
    
    array = list()
    maximum = 0

    for _ in range(n):
        row = list(map(int, input().split()))
        maximum += sum(row)
        array.append(row)
        
    for i in range(0, maximum):
        visited = [[False for _ in range(m)] for _ in range(n)]
        cnt = count_elements(array, visited)
        if cnt <= 1:
            array = melt(array)
        else:
            return i
    
    return 0

answer = main()
print(answer)