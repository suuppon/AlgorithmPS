n = int(input())
A = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

A.sort()

def binary_search(arr, x):
    start = 0
    end = n-1
    answer = 0
    
    while start <= end:
        mid = (start + end) // 2
        
        if x > arr[mid]:
            start = mid + 1
        elif x < arr[mid]:
            end = mid - 1
        else:
            answer = 1
            break
    
    return answer
    
for item in arr:
    print(binary_search(A, item))