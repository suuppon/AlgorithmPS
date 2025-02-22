import sys
input = sys.stdin.readline

n, h = map(int, input().split())

down, up = list(), list()

for i in range(n):
    obs = int(input())
    if i % 2 == 1:
        up.append(obs)
    else:
        down.append(obs)

up.sort()
down.sort()

def count_obstacle(array, target_height):
    start, end = 0, len(array) -1 
    
    while start <= end:
        mid = (start + end) // 2
        
        elt = array[mid]
        
        if elt < target_height:
            start = mid + 1
        else:
            end = mid - 1
            
    return start

minimum = n
cnt = 0

for i in range(1, h+1):
    down_cnt = len(down) - count_obstacle(down, i-0.5)
    up_cnt = len(up) - count_obstacle(up, h-i+0.5)
    
    if down_cnt + up_cnt < minimum:
        minimum = down_cnt + up_cnt 
        cnt = 1
    elif down_cnt + up_cnt == minimum:
        cnt += 1
        
print(minimum, cnt)