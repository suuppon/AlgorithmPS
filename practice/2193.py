dp_table = [0] * 91

dp_table[1] = 1 # 1
dp_table[2] = 1 # 10

nums_endswithzero = [0 for _ in range(91)]
nums_endswithone = [0 for _ in range(91)]

nums_endswithzero[3] = 1 # 100
nums_endswithone[3] = 1 # 101
dp_table[3] = 2 # 100, 101

for i in range(4, 91):
    nums_endswithzero[i] = nums_endswithzero[i-1] + nums_endswithone[i-1]
    nums_endswithone[i] = nums_endswithzero[i-1]
    dp_table[i] = nums_endswithone[i] + nums_endswithzero[i]
    
N = int(input())

print(dp_table[N])