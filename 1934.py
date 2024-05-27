import sys
from math import lcm

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(lcm(a,b))