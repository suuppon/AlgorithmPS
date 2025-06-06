import sys
input = sys.stdin.readline

n, k = map(int, input().split())

goods_list = list()

for _ in range(n):
    w, v = map(int, input().split())
    goods_list.append((w, v))

dp_table = [0 for _ in range(k+1)]

for i in range(k, 1, -1):
    for g in goods_list:
        w, v = g
        if i - w < 0:
            continue
        else:
            dp_table[i] = max(dp_table[i], dp_table[i-w] + v)

print(max(dp_table))