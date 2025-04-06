dp_table = [0 for _ in range(31)]

dp_table[2] = 3

for i in range(4, 31, 2):
    num = i // 2 - 1
    dp_table[i] = 2
    for j in range(num):
        if j == 0:
            mult = 3
        else:
            mult = 2
        dp_table[i] += mult * dp_table[i - 2*(j+1)]

n = int(input())
print(dp_table[n])