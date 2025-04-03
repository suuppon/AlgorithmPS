import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

def bfs(start):
    # distance[n] : start부터 n까지 걸리는 시간
    distance = [-1 for _ in range(100001)]
    queue = deque([(0, start)])
    distance[start] = 0
    
    time = int(1e9)
    cnt = 0
    
    while queue:
        curTime, curNode = queue.popleft()
        
        if time < curTime:
            break
        
        if curNode == K:
            time = curTime
            cnt += 1
            
        for n in [curNode+1, curNode-1, curNode*2]:
            if 0 <= n <= 100000 and (distance[n]==-1 or distance[n] >= distance[curNode]+1):
                queue.append((curTime+1, n))
                distance[n] = curTime+1
    
    return time, cnt

time, cnt = bfs(N)

print(time)
print(cnt)