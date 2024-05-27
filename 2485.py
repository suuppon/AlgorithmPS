import sys
from math import gcd

input = sys.stdin.readline

n = int(input())

tree_0 = int(input())
distance_list = list()

for _ in range(n-1):
    tree = int(input())
    distance_list.append(abs(tree-tree_0))
    tree_0 = tree

g = gcd(distance_list[0], distance_list[1])

if len(distance_list) >= 3:
    for i in range(2, len(distance_list)):
        g = gcd(g, distance_list[i])

c = 0
for distance in distance_list:
    c += int(distance/g) - 1

print(c)

