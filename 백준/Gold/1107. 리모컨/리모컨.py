import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

broken = set()

if M:
    broken = set(map(int, input().split()))

def brute_force():
    min_cnt = abs(N-100)
    
    for num in range(1000001):
        impossible = False
        # num : 리모컨으로 누른 버튼
        for digit in str(num):
            if int(digit) in broken:
                impossible = True
                
        if impossible:
            continue
        
        cnt = len(str(num))
        cnt += abs(N - num)
        
        min_cnt = min(min_cnt, cnt)
            
    return min_cnt
        
print(brute_force())