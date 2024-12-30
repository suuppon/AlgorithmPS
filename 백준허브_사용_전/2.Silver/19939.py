import sys
input = sys.stdin.readline

n, k = map(int, input().split())

sum = k*(k+1) // 2

if n - sum >= 0:
    last = (n-sum) % k
    if last == 0:
        print(k-1)
    else:
        print(k)

else:
    print(-1)