import sys
input = sys.stdin.readline
import collections

def get(n:int, line:collections.deque):
    line_1 = list()

    for i in range(1,n+1):
        while len(line) > 0:
            if len(line_1) != 0:
                tail = line_1.pop()
                if tail == i:
                    break
                elif tail != i:
                    line_1.append(tail)
            
            head = line.popleft()
            if head != i:
                line_1.append(head)
            else:
                break
        
        if len(line) == 0:
            break


    for i in range(len(line_1)-1):
        if line_1[i] -1 != line_1[i+1]:
            return 'Sad'
        else:
            pass
    
    return 'Nice'

N = int(input())

line = collections.deque(list(map(int, input().split())))

line_1 = get(n=N, line=line)

print(line_1)