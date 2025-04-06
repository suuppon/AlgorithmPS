n, k = map(int, input().split())

value_list = [int(input()) for _ in range(n)]

dp_table = [-1 for _ in range(k+1)]

for v in value_list:
    if v <= k:
        dp_table[v] = 1

for i in range(2, k+1):
    tmp_minimum = 10**9
    for v in value_list:
        if i - v >= 0 and dp_table[i-v] >= 0:
            tmp_minimum = min(dp_table[i-v] + 1, tmp_minimum)
    if dp_table[i] >= 0:
        dp_table[i] = min(tmp_minimum, dp_table[i])
    elif tmp_minimum != 10**9:
        dp_table[i] = tmp_minimum
    else:
        dp_table[i] = -1

print(dp_table[-1])