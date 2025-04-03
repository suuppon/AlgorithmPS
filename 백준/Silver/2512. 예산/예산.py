import sys
input = sys.stdin.readline

n = int(input())
requests = list(map(int, input().split()))
m = int(input())

start = 0
end = max(requests)
answer = 0

while start <= end:
    mid = (start + end) //2
    
    budget = sum(min(r, mid) for r in requests)
        
    if budget <= m:
        answer = mid
        start = mid+1
    else:
        end = mid-1

print(answer)