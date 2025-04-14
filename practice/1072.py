x, y = map(int, input().split())

z = (y * 100) // x

start = 0
end = 10**13

answer = -1
while start <= end:
    mid = (start + end) // 2
    
    if z < ((y + mid) * 100) // (x + mid):
        answer = mid
        end = mid - 1
        
    else:
        start = mid + 1
        
print(answer)