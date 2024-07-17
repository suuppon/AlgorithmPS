n = int(input())

def stair_num():
    arr = [0 for _ in range(101)]
    
    arr[1] = 9
    arr[2] = 17
    
    for i in range(3, len(arr)):
        arr[i] = 2*arr[i-1] - 2
        
    return arr
    
print(stair_num()[n])