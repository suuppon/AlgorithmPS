n = int(input())
arr = list(map(int, input().split()))

dp_table = [0 for _ in range(n+1)]

dp_table[1] = arr[0]

for i in range(2, n+1):
    for idx, p in enumerate(arr):
        num = idx + 1
        if i - num < 0:
            continue
        else:
            dp_table[i] = max(dp_table[i], dp_table[i-num] + p)
        
print(dp_table[n])