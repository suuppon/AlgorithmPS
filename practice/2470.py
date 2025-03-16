n = int(input())

arr = list(map(int, input().split()))

arr.sort()

left, right = 0, n-1

minimum = 10**10
liquid_1, liquid_2 = 0, 0

while left < right:
    sum = arr[left] + arr[right]
    if abs(sum) <= minimum:
        minimum = abs(sum)
        liquid_1, liquid_2 = arr[left], arr[right]
        
    if sum < 0:
        left += 1
        
    elif sum > 0:
        right -= 1
        
    else:
        liquid_1, liquid_2 = arr[left], arr[right]
        break

print(liquid_1, liquid_2)