import sys
input = sys.stdin.readline

n = int(input())
dp_table = [0 for _ in range(n)]

calander = list()
for _ in range(n):
    t, p = map(int, input().split())
    calander.append((t, p))
    
dp_table[-1] = calander[-1][1] if calander[-1][0] <= 1 else 0

for i in range(2, n+1):
    index = -i
    if index + calander[index][0] > 0:
        dp_table[index] = dp_table[index + 1]
    else:
        dp_table[index] = max(dp_table[index+1], calander[index][1] + dp_table[index + calander[index][0]])

print(dp_table[0])