from collections import deque

def bfs_collect(arr, rs, cs, visited):
    elt = arr[rs][cs]
    queue = deque([(rs, cs)])
    visited[rs][cs] = True
    idx_set = {(rs, cs)}
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if (
                0 <= nr < 12 and 0 <= nc < 6
                and not visited[nr][nc]
                and arr[nr][nc] == elt
            ):
                visited[nr][nc] = True
                queue.append((nr, nc))
                idx_set.add((nr, nc))
    return idx_set


def apply_gravity(arr):
    for c in range(6):
        stack = []
        for r in range(11, -1, -1):
            if arr[r][c] != '.':
                stack.append(arr[r][c])
        for r in range(11, -1, -1):
            if stack:
                arr[r][c] = stack.pop(0)
            else:
                arr[r][c] = '.'


if __name__ == "__main__":
    arr = [list(input().strip()) for _ in range(12)]
    pop_cnt = 0
    
    while True:
        visited = [[False] * 6 for _ in range(12)]
        to_explode = set()
        
        for i in range(12):
            for j in range(6):
                if arr[i][j] != '.' and not visited[i][j]:
                    cluster = bfs_collect(arr, i, j, visited)
                    if len(cluster) >= 4:
                        to_explode |= cluster
                        
        if not to_explode:
            break
        
        pop_cnt += 1
        
        for r, c in to_explode:
            arr[r][c] = '.'
            
        apply_gravity(arr)
        
    print(pop_cnt)