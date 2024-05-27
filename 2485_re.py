import sys
input = sys.stdin.readline
import math

n = int(input())
distance_list = list()

tree1 = int(input())
for _ in range(n-1):
    tree2 = int(input())
    
    distance_list.append(tree2-tree1)
    tree1 = tree2

gcd = math.gcd(distance_list[0], distance_list[1])

for i in range(1, n-2):
    gcd = math.gcd(math.gcd(distance_list[i], distance_list[i+1]), gcd)
    
c = 0

for distance in distance_list:
    c += int(distance/gcd)-1

print(c)