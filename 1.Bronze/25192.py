import sys
input = sys.stdin.readline

n = int(input())

users = set()
c = 0

for i in range(n):
    chat = input().rstrip()
    if chat == "ENTER":
        c += len(users)
        users = set()
    else:
        users.add(chat)

c += len(users)

print(c)