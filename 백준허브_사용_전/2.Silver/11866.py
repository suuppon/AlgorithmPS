import sys
input = sys.stdin.readline
import collections

n, k = map(int, input().split())
num_list = [i for i in range(1, n+1)]
List = list()
idx = 0

while len(num_list) > 0:
    next = (idx + k-1) % len(num_list)

    List.append(num_list.pop(next))
    idx = next

print('<', end='')
for i in range(len(List)-1):
    print("{}, ".format(List[i]), end='')
print("{}".format(List[-1]), end='')
print('>')