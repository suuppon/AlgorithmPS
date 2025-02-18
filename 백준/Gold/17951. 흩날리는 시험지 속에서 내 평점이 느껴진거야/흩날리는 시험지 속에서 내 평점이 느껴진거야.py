n, k = map(int, input().split())

score_list = list(map(int, input().split()))

start = min(score_list)
end = sum(score_list)
answer = 0

while start <= end:
    mid = (start + end) // 2
    
    tmp = 0
    cnt = 0
    
    for score in score_list:
        tmp += score
        if tmp >= mid:
            cnt += 1
            tmp = 0
            
    if cnt >= k:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)