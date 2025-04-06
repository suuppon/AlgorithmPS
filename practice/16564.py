import sys
input = sys.stdin.readline

n, k = map(int, input().split())

level_list = [int(input()) for _ in range(n)]

start = 0
end = 10 ** 10
answer = 0

while start <= end:
    mid = (start + end) // 2
    
    tmp_k = k
    
    for x in level_list:
        if mid > x:
            tmp_k -= mid - x
    
    if tmp_k < 0:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)