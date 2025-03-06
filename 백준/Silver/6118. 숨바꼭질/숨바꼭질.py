from collections import deque

n, m = map(int, input().split())

arr = [list() for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    
    
visited = [False for _ in range(n+1)]

queue = deque([(1, 0)])

maximum = 0
barn_list = []

while queue:
    elt = queue.popleft()
    
    num, dist = elt[0], elt[1]
    if visited[num]:
        continue
    else:
        visited[num] = True
    
    if dist == maximum:
        barn_list.append(num)
    elif dist > maximum:
        barn_list = [num]
        maximum = dist
    
    for barn in arr[num]:
        queue.append((barn, dist+1))

barn_list.sort()
print(barn_list[0], maximum, len(barn_list))