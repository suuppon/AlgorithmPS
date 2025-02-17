import sys
input = sys.stdin.readline

n, m = map(int, input().split())
minutes_list = list(map(int, input().split()))

start = max(minutes_list)
end = sum(minutes_list)

answer = 0

def count_num(arr, length):
    length_origin = length
    
    cnt = 1
    
    for i in range(n):
        item = arr[i]
        length -= item
        if length >= 0:
            continue
        else:
            cnt += 1
            length = length_origin
            length -= item
    
    return cnt

while start <= end:
    mid = (start + end) // 2
    cnt = count_num(minutes_list, mid)
    if cnt <= m:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1
        
print(answer)