import sys
input = sys.stdin.readline

n, k = map(int, input().split())

value_list = list()
for _ in range(n):
    value_list.append(int(input()))

dp_table = [0 for _ in range(k+1)]
dp_table[0] = 1
    
for value in value_list:
    for i in range(value, k+1):
        dp_table[i] += dp_table[i-value]

print(dp_table[-1])