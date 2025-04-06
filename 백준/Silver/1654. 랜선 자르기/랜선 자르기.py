k, n = map(int, input().split())

arr = list()

for _ in range(k):
    arr.append(int(input()))
    
def binary_search(arr, start, end, target):
    
    while start <= end:
        mid = (start + end) // 2
        num = 0
        
        for item in arr:
            num += item // mid
        
        if num >= target:
            answer = mid
            start = mid + 1
        
        elif num < target:
            end = mid -  1
    
    return answer


start = 1
end = max(arr)
target = n

print(binary_search(arr, start, end, target))