n, m = map(int, input().split())

time_list = list()

for _ in range(n):
    t = int(input())
    time_list.append(t)
    
start = 0
end = min(time_list) * m

answer = 0

while start <= end:
    target = m
    mid = (start + end) // 2
    
    for t in time_list:
        target -= mid // t
        
    if target <= 0:
        answer = mid
        end = mid - 1
    
    else:
        start = mid + 1
        
print(answer)