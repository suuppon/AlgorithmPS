from itertools import combinations

n, k = map(int, input().split())

houses = []

for i in range(n):
    x,y = map(int, input().split())
    houses.append([x,y])

Comb = list(combinations(houses, k))


comb_list = list()
max_distance_list  = 1e10
for comb in Comb:
    max_distance = 1e10
    distance_list = []
    for house in houses:
        distance = 1e10
        for point in comb:
            distance_new = abs(house[0]-point[0])+abs(house[1]-point[1])
            if distance >= distance_new:
                distance = distance_new
        distance_list.append(distance)
        if max(distance_list) < max_distance:
            max_distance = max(distance_list)
    if max_distance_list >= max(distance_list):
        max_distance_list = max(distance_list)
        selected_comb = comb
    
print(max_distance_list)