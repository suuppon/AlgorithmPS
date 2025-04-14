n = int(input())
arr = list(map(int, input().split()))

arr.sort()

def check_good(arr, idx):
    target = arr[idx]
    start, end = 0, n-1
    answer = 0
    
    while start < end:
        if arr[start] + arr[end] < target:
            start += 1
        elif arr[start] + arr[end] > target:
            end -= 1
        else:
            if start == idx:
                start +=1
            elif end == idx:
                end -= 1
            else:
                answer = 1
                break
            
    return answer

cnt = 0

for i in range(n):
    cnt += check_good(arr, i)

print(cnt)