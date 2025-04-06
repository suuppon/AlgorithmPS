str1 = list(input())
str2 = list(input())
len_1, len_2 = len(str1), len(str2)

dp_table = [[0 for _ in range(len_1+1)] for _ in range(len_2+1)]

for i in range(len_1):
    for j in range(len_2):
        if str1[i] == str2[j]:
            dp_table[j+1][i+1] = dp_table[j][i] + 1
        else:
            dp_table[j+1][i+1] = max(dp_table[j][i+1], dp_table[j+1][i])

print(dp_table[-1][-1])