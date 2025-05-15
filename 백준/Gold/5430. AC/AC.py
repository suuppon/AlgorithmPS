import sys
import ast
from collections import deque

input = sys.stdin.readline

T = int(input())

def process(p, arr):
    dq = deque(arr)
    reversed_flag = False

    for cmd in p:
        if cmd == 'R':
            reversed_flag = not reversed_flag
        elif cmd == 'D':
            if not dq:
                return 'error'
            if reversed_flag:
                dq.pop()
            else:
                dq.popleft()

    if reversed_flag:
        dq = reversed(dq)

    return '[' + ','.join(map(str, dq)) + ']'

for _ in range(T):
    p = input().strip()
    n = int(input())
    arr = ast.literal_eval(input().strip())
    print(process(p, arr))