import sys
input = sys.stdin.readline

def ParenthesesCheck(string):
    arr = list()

    for char in string:
        if char == '(':
            arr.append(0)
        elif char == ')':
            if len(arr) == 0:
                return 'no'
            else:
                if arr.pop() == 0:
                    pass
                else:
                    return 'no'

        elif char == '[':
            arr.append(1)
        elif char == ']':
            if len(arr) == 0:
                return 'no'
            else:
                if arr.pop() == 1:
                    pass
                else:
                    return 'no'
        else:
            pass

    if len(arr) == 0 and len(arr) == 0:
        return 'yes'
    else:
        return 'no'
    
while True:
    string = input().rstrip()
    if string == '.':
        break
    
    print(ParenthesesCheck(string=string))