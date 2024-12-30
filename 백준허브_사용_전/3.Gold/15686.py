import sys
input = sys.stdin.readline

from itertools import combinations

n, m = map(int, input().split())

city = list()
for _ in range(n):
    row = list(map(int, input().split()))
    city.append(row)
    
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

result = 1e10
for comb in combinations(chicken, m):
    chicken_distance_temp = 0
    for h in house:
        min_distance = 1e10
        for j in range(m):
            min_distance = min(min_distance, abs(h[0] - comb[j][0]) + abs(h[1] - comb[j][1]))
        chicken_distance_temp += min_distance
    result = min(result, chicken_distance_temp)
    
print(result)