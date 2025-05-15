T = int(input())

def main():
    N = int(input())
    coin_list = list(map(int, input().split()))
    M = int(input())
    
    dp = [0 for _ in range(M+1)]
    dp[0] = 1
    
    for coin in coin_list:
        for j in range(coin, M+1):
            dp[j] += dp[j-coin]
    
    return dp[-1]

for _ in range(T):
    print(main())