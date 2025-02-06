n = int(input())
num_list = list(map(int, input().split()))

num_set = set(num_list)
num_list_2 = list(num_set)
num_list_2.sort()

idx_dict = {}

for i in range(len(num_list_2)):
    idx_dict[num_list_2[i]] = i
    
for num in num_list:
    print(idx_dict[num], end=' ')