import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

train = [deque([0] * 20) for _ in range(N + 1)]

for idx in range(M):
    cmd, *args = map(int, input().split())
    if cmd in (1, 2):
        i, x = args
    else:
        i = args[0]
        
    if cmd == 1:
        train[i][x-1] = 1
        
    elif cmd == 2:
        train[i][x-1] = 0
        
    elif cmd == 3:
        train[i].appendleft(0)
        train[i].pop()
        
    elif cmd == 4:
        train[i].append(0)
        train[i].popleft()
        
answer = set()
for i in range(1, N + 1):
    answer.add(tuple(train[i]))
print(len(answer))