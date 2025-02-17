import math

T = int(input())

for i in range(T):
    arr = list(map(float,input().split()))
    dist = math.sqrt(((arr[0]-arr[3])**2+(arr[1]-arr[4])**2))
    rad_sum = arr[2]+arr[5]
    if arr[0] == arr[3] and arr[1] == arr[4] and arr[2] == arr[5]:
        print(-1)
    elif dist + min(arr[2],arr[5]) < max(arr[2],arr[5]):
        print(0)
    elif dist + min(arr[2],arr[5]) ==  max(arr[2],arr[5]):
        print(1)
    else:
        if dist > rad_sum:
            print(0)
        elif dist == rad_sum:
            print(1)
        elif dist < rad_sum:
            print(2)