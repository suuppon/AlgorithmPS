n, m = map(int, input().split())

height_list = list(map(int, input().split()))

height_list.sort()

def binary_search(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for item in arr:
            if item > mid:
                total += item - mid
                
        if total < m:
            end = mid - 1
        else:
            start = mid + 1
            result = mid
    
    return result
    
start = 0
end = max(height_list)
target = m

print(binary_search(height_list, start, end, target))
