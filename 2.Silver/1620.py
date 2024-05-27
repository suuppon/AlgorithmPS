import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dic = dict()

for i in range(1, n+1):
    name = input().rstrip()
    dic[i] = name
    dic[name] = i


for _ in range(m):
    check = input().rstrip()

    if check.isdigit():
        Name = dic[int(check)]
        print(Name)
    else:
        Num = dic[check]
        print(Num)