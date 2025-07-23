from collections import deque

N, M, K = map(int, input().split())

hallway = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    hallway[r-1][c-1] = 1
    
def bfs(r, c, visited):
    cnt = 1
    queue = deque([(r, c)])
    visited[r][c] = True
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            if (0 <= nr < N and 0 <= nc < M) and not visited[nr][nc] and hallway[nr][nc] == 1:
                cnt += 1
                queue.append((nr, nc))
                visited[nr][nc] = True
    
    return cnt

visited = [[False for _ in range(M)] for _ in range(N)]
maximum = 0

for r in range(N):
    for c in range(M):
        if not visited[r][c] and hallway[r][c] == 1:
            cnt = bfs(r, c, visited)
            maximum = max(cnt, maximum)
            
print(maximum)