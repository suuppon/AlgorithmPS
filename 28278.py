import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.List = list()
    
    def command_1(self, X):
        self.List.append(X)
    
    def command_2(self):
        if self.command_3() == 0:
            return -1
        else:
            return self.List.pop()

    def command_3(self):
        return len(self.List)
    
    def command_4(self):
        if self.command_3() == 0:
            return 1
        else:
            return 0
        
    def command_5(self):
        if self.command_3() == 0:
            return -1
        else:
            return self.List[-1]
        

stack = Stack()

N = int(input())

for _ in range(N):
    command = input().rstrip()

    if command.startswith('1'):
        command, X = command.split()
        stack.command_1(X=X)
    elif command == '2':
        print(stack.command_2())
    elif command == '3':
        print(stack.command_3())
    elif command == '4':
        print(stack.command_4())
    elif command == '5':
        print(stack.command_5())

