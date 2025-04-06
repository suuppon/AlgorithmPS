import sys
input = sys.stdin.readline

N, M = map(int, input().split())

seq = list(int(input()) for _ in range(N))

seq.sort()

answer = int(1e10)
left = 0
right = 0

while left <= right and right <= N-1:
    dif = seq[right] - seq[left]
    
    if dif >= M:
        left += 1
        answer = min(dif, answer)
    else:
        right += 1
        
print(answer)