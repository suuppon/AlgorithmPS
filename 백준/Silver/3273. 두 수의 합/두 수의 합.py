import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

start = 0
end = n-1

cnt = 0

arr.sort()

while start < end:
    tmp = arr[start] + arr[end]
    if tmp == x:
        cnt += 1
        start += 1
    elif tmp > x:
        end -= 1
    else:
        start += 1
        
print(cnt)