import sys
input = sys.stdin.readline

n = int(input())

distance_list = list(map(int, input().split()))
oil_cost_list = list(map(int, input().split()))

oil = 0
cost = 0

for i in range(n-1):
    if oil_cost_list[i] == min(oil_cost_list):
        cost += (distance_list[i] - oil) * oil_cost_list[i]
        oil += sum(distance_list[i:n-1])
    if oil < distance_list[i]:
        cost += (distance_list[i] - oil) * oil_cost_list[i]
        oil += distance_list[i] - oil

print(cost)