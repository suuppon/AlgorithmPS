import sys
input = sys.stdin.readline

N = int(input())

def PS_stack(PS):
    arr = list()
    for string in PS:
        if string == '(':
            arr.append(0)
        elif string == ')':
            if len(arr) == 0:
                return 'NO'
            else:
                arr.pop()

    if len(arr) == 0:
        return 'YES'
    else:
        return 'NO'


for _ in range(N):
    PS = input().rstrip()
    print(PS_stack(PS=PS))

