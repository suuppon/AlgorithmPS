import sys
import collections
input = sys.stdin.readline

queue = collections.deque()

n = int(input())

for _ in range(n):
    command = input().rstrip()

    if 'push' in command:
        command, x = command.split()
        queue.append(x)
    
    elif command == 'pop':
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
            
    elif command == 'size':
        print(len(queue))

    elif command == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif command == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)