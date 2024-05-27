import sys
input = sys.stdin.readline

n, m = map(int, input().split())

set1 = set()
set2 = set()

for _ in range(n):
    name_1 = input().rstrip()
    set1.add(name_1)

for _ in range(m):
    name_2 = input().rstrip()
    set2.add(name_2)

int_set = list(set1.intersection(set2))

int_set.sort()
print(len(int_set))

for name in int_set:
    print(name)