from math import sqrt
INF = int(1e9)

maximum = int(1e5)
maximum_sqrt = int(sqrt(maximum))

dp = [INF for _ in range(maximum+1)]

for i in range(1, maximum_sqrt+1):
    dp[i**2] = 1
    
    
for i in range(1, maximum+1):
    greatest_square_num = int(sqrt(i))
    
    for num in range(1, greatest_square_num):
        dp[i] = min(dp[i], dp[i-num**2] + 1)
        
        
print(dp[int(input())])