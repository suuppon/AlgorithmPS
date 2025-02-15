n, m, l = map(int, input().split())

cutting_point = list()

for _ in range(m):
    cutting_point.append(int(input()))

cutting_point.append(l)

def calculate_cnt(cutting_point, length):
    cnt = 0
    tmp_length = 0
    for p in cutting_point:
        if p - tmp_length >= length:
            cnt += 1
            tmp_length = p
            
    return cnt

def binary_search(length, cutting_point, cutting_num):
    cutting_point.sort()
    
    start = 0
    end = length
    answer = 0
    
    while start <= end:
        mid = (start + end) // 2
        
        cnt = calculate_cnt(cutting_point, mid)
        
        if cnt >= cutting_num+1:
            answer = mid
            start = mid + 1
            
        else:
            end = mid - 1
    
    return answer

for _ in range(n):
    q = int(input())
    print(binary_search(length=l, cutting_point=cutting_point, cutting_num=q))