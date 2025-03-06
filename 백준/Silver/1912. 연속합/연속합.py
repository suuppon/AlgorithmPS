import sys
input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))

dp_table = [0 for _ in range(n+1)]
dp_table[0] = -1001

for i in range(1, n+1):
    dp_table[i] = max(dp_table[i-1] + sequence[i-1], sequence[i-1])

print(max(dp_table))