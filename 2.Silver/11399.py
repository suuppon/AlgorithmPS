import sys
input = sys.stdin.readline

n = int(input())

time_list = list(map(int, input().split()))
time_list.sort()
sum_time_list = [0]

for i in range(n):
    sum_time_list.append(sum_time_list[i]+time_list[i])

print(sum(sum_time_list))