import sys
input = sys.stdin.readline

N, M = map(int, input().split())

food_dict = dict()

for i in range(M):
    l_j, *food = map(int, input().split())
    for k in range(l_j):
        if food[2*k] in food_dict.keys():
            food_dict[food[2*k]].append((i+1, food[2*k+1]))
        else:
            food_dict[food[2*k]] = [(i+1, food[2*k+1])]
    

food_dp = [[0, 0] for _ in range(N+1)]

answer = 0
for food in food_dict.keys():
    idx = 2
    tmp_j = -1
    for j, v in food_dict[food]:
        if tmp_j == j - 1:
            food_dp[food].append(max(food_dp[food][idx-2]+v, food_dp[food][idx-1]))
        else:
            food_dp[food].append(food_dp[food][idx-1]+v)
            
        tmp_j = j
        idx += 1
    answer += max(food_dp[food])
    
print(answer)