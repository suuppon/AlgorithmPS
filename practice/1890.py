n = int(input())

arr = list()
cnt = 0

for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
dp[1][1] = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == n and j == n:
            break
        elt = arr[i-1][j-1]
        
        if i + elt <= n:
            dp[i+elt][j] += dp[i][j]
        if j + elt <= n:
            dp[i][j+elt] += dp[i][j]
            
print(dp[-1][-1])