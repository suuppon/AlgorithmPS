import sys

input = sys.stdin.readline

n = input().rstrip()
n = int(n)

num_list = list(map(int, input().split()))
num_set = set(num_list)
dic = dict()
for item in num_set:
    dic[item] = 0

for item in num_list:
    dic[item] += 1

m = input().rstrip()
m = int(m)

check_list = list(map(int, input().split()))

for num in check_list:
    if num in dic.keys():
        print(dic[num], end=' ')
    else:
        print(0, end = ' ')