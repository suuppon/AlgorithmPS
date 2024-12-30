import sys
input = sys.stdin.readline

import collections
deque = collections.deque()

n = int(input())

for _ in range(n):
    command = input().rstrip()

    if command.startswith('1') == True:
        command, x = command.split()
        deque.appendleft(x)

    elif command.startswith('2') == True:
        command, x = command.split()
        deque.append(x)
    

    elif command == '3':
        if len(deque) != 0:
            print(deque.popleft())
        else:
            print(-1)
            
    elif command == '4':
        if len(deque) != 0:
            print(deque.pop())
        else:
            print(-1)

    elif command == '5':
        print(len(deque))

    elif command == '6':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif command == '7':
        if len(deque) != 0:
            print(deque[0])
        else:
            print(-1)
    elif command == '8':
        if len(deque) != 0:
            print(deque[-1])
        else:
            print(-1)