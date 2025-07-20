s = input()
stack = []

for i in s:
    if i == '(' or i == '[':
        stack.append(i)
    elif i == ')':
        tmp = 0
        while stack:
            top = stack.pop()
            if top == '(':
                stack.append(2 if tmp == 0 else 2 * tmp)
                break
            elif isinstance(top, int):
                tmp += top
            else:
                print(0)
                exit(0)
        else:
            # 괄호 여는 거 못 만남
            print(0)
            exit(0)

    elif i == ']':
        tmp = 0
        while stack:
            top = stack.pop()
            if top == '[':
                stack.append(3 if tmp == 0 else 3 * tmp)
                break
            elif isinstance(top, int):
                tmp += top
            else:
                print(0)
                exit(0)
        else:
            print(0)
            exit(0)

# 마지막에도 잘못된 게 남아있으면 안 됨
result = 0
for i in stack:
    if isinstance(i, int):
        result += i
    else:
        print(0)
        exit(0)

print(result)