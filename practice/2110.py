n, c = map(int, input().split())

house_coord = list(int(input()) for _ in range(n))

house_coord.sort()

start = 1
end = house_coord[-1] - house_coord[0]

answer = 0

while start <= end:
    cur = house_coord[0]
    cnt = 1
    
    mid = (start + end) // 2
    
    for i in range(1, n):
        if house_coord[i] - cur >= mid:
            cur = house_coord[i]
            cnt += 1
    
    if cnt >= c:
        start = mid + 1
        answer = mid
    elif cnt < c:
        end = mid - 1
        
print(answer)