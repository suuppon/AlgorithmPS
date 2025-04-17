import sys 
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, K = map(int, input().split())
    num_set = set(map(int, input().split()))
    
    checked = set()
    start = 0
    end = max(num_set) - min(num_set)
    answer = 0
    
    while start < end:
        cnt = 0
        mid = (start + end) // 2
        for elt in num_set:
            dif = mid - elt
            if dif in num_set and dif not in checked:
                cnt += 1
                checked.add(dif)
            checked.add(elt)
        
        if cnt > 0:
            answer = cnt
            end = mid - 1
        else:
            start = mid + 1
    
    print(answer)