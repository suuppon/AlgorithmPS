import sys

input = sys.stdin.readline

class Stack:
    def __init__(self, capacity=100000):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.top_index = -1

    def push(self, data):
        if self.top_index + 1 == self.capacity:
            return "Stack is full"
        self.top_index += 1
        self.arr[self.top_index] = data

    def pop(self):
        if self.empty():
            return -1
        popped_value = self.arr[self.top_index]
        self.arr[self.top_index] = None
        self.top_index -= 1
        return popped_value

    def size(self):
        return self.top_index + 1

    def empty(self):
        return self.size() == 0

    def top(self):
        if self.empty():
            return -1
        else:
            return self.arr[self.top_index]

n = int(input())
stack = Stack()

for _ in range(n):
    command = input().rstrip()

    if 'push' in command:
        _, value = command.split()
        stack.push(int(value))
    elif command == 'pop':
        print(stack.pop())
    elif command == 'empty':
        print(int(stack.empty()))
    elif command == 'size':
        print(stack.size())
    elif command == 'top':
        print(stack.top())
