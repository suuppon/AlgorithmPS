n, m = map(int, input().split())

arr = [int(input()) for _ in range(n)]

def binary_search(arr, start, end, target):
    
    while start <= end:
        mid = (start + end) // 2

        k = find_k(arr, mid)
        
        if k <= target:
            answer = mid
            end = mid - 1
        
        else:
            start = mid + 1
    
    return answer
    
def find_k(arr, x):
    x_original = x
    cnt = 1
    for item in arr:
        if x >= item:
            x -= item
        else:
            x = x_original
            cnt += 1
            x -= item
    
    return cnt

start = max(arr)
end = sum(arr)

target = m

print(binary_search(arr, start, end, target))
