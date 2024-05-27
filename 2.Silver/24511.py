import sys
input = sys.stdin.readline
import collections  

n = int(input())

Stack_and_Queue = list(map(int, input().split()))
QueueStack = list(map(int, input().split()))
m = int(input())
seq = list(map(int,input().split()))

Queue_index = list()

returns = collections.deque()

for i in range(n):
    if Stack_and_Queue[i] == 0:
        returns.appendleft(QueueStack[i])

for j in range(m):
    returns.append(seq[j])
    x = returns.popleft()
    print(x, end=' ')