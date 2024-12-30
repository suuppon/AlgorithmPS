import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coin_list = list()

for _ in range(n):
    coin = int(input())
    coin_list.append(coin)

coin_list.sort(reverse=True)

c = 0

for coin in coin_list:
    if k == 0:
        break
    
    if k - coin < 0:
        pass
    else:
        num = k // coin
        k -= num*coin
        c += num
    
print(c)