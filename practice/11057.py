n = int(input())

dp_table = [[0 for _ in range(10)] for _ in range(1001)]

for i in range(10):
    dp_table[1][i] = 1

for i in range(1001):
    dp_table[i][0] = 1
    
for i in range(2, 1001):
    for j in range(1, 10):
        dp_table[i][j] = dp_table[i-1][j] + dp_table[i][j-1]
        
print(sum(dp_table[n]) % 10007)