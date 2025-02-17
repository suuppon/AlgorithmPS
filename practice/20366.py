from itertools import combinations

n = int(input())

arr = list(map(int, input().split()))

comb = combinations(range(n), 2)

height_list = list()

for c in comb:
    height_list.append(arr[c[0]] + arr[c[1]])