dp_table = [[0 for _ in range(10)] for _ in range(101)]

for i in range(1, 10):
    dp_table[1][i] = 1

for i in range(2, 101):
    for j in range(10):
        if j == 0:
            left, right = 0, dp_table[i-1][j+1]
        elif j == 9:
            left, right = dp_table[i-1][j-1], 0
        else:
            left, right = dp_table[i-1][j-1], dp_table[i-1][j+1]

        dp_table[i][j] = left + right
n = int(input())

print(sum(dp_table[n]) % 1000000000)