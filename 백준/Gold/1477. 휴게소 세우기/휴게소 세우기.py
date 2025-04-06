import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
arr = list(map(int, input().split()))
arr = arr + [0, l]

start = 1
end = l-1

arr.sort()

answer = 0
while start <= end:
    mid = (start + end) // 2
    
    cnt = 0
    for i in range(len(arr) - 1):
        dist = arr[i+1] - arr[i] - 1
        tmp_cnt = dist // mid
        tmp_rem = dist % mid

        cnt += tmp_cnt
    
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid

print(answer)