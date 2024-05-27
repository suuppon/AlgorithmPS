import sys
input = sys.stdin.readline
import collections

N = int(input())

queue = collections.deque([i for i in range(1, N+1)])

while len(queue) > 1:
    queue.popleft()
    tmp = queue.popleft()
    queue.append(tmp)

print(queue[0])