n, m = map(int, input().split())

arr = list()

dp_table = [[0 for _ in range(m+1)] for _ in range(n+1)]

for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    
for i in range(1, n+1):
    for j in range(1, m+1):
        dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1]) + arr[i-1][j-1]
    
print(dp_table[-1][-1])