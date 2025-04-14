N, M = map(int, input().split())
sr, sc, sd = map(int, input().split())

# direction
# 0 : 북, 1 : 동, 2 : 남, 3 : 서
table = list()
for _ in range(N):
    table.append(list(map(int,input().split())))
    
dr_list = [-1, 0, 1, 0]
dc_list = [0, 1, 0, -1]
r, c, d = sr, sc, sd
cnt = 0

while True:
    if table[r][c] == 0:
        table[r][c] = 2 #2는 청소표시
        cnt += 1
    
    dirty = False
    for dr, dc in zip(dr_list, dc_list):
        nr, nc = r + dr, c + dc
        if not (0 <= nr < N and 0 <= nc < M):
            continue
        
        if table[nr][nc] == 0:
            dirty = True
            break
    
    if not dirty:
        opposite_dir = (d + 2) % 4
        if table[r + dr_list[opposite_dir]][c + dc_list[opposite_dir]] == 1:
            break
        
        else:
            r, c = r + dr_list[opposite_dir], c + dc_list[opposite_dir]
    else:
        for _ in range(4):
            d = (d-1) % 4
            nr, nc = r + dr_list[d], c + dc_list[d]
            
            if table[nr][nc] == 0:
                r, c = nr, nc
                break
              
print(cnt)