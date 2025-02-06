from itertools import combinations

n = int(input())
num_list = list(map(int, input().split()))

cnt = 0

for i in range(n-1):
    if num_list[i] > num_list[i+1]:
        new_list = num_list[:i] + num_list[i+1:]
        
        
print(cnt)