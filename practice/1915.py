import sys
input = sys.stdin.readline
import math

n, m = map(int, input().split())

arr = [input().rstrip() for _ in range(n)]

dp_table = [[0 for _ in range(m)] for _i in range(n)]

square = False
for i in range(n):
    for j in range(m):
        row = arr[i]
        if i == 0 or j == 0:
            if row[j] == '1':
                dp_table[i][j] = 1
        else:
            if row[j] == '1':
                dp_table[i][j] = min(dp_table[i-1][j-1], dp_table[i-1][j], dp_table[i][j-1]) + 1
                  
maximum = 0

for i in range(n):
    maximum = max(max(dp_table[i]), maximum)

print(maximum ** 2)