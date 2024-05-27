import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num_list = list(map(int, input().split()))
sum_num_list = [0]
tmp = 0

for num in num_list:
    tmp += num
    sum_num_list.append(tmp)

for _ in range(m):
    s, e = map(int, input().split())
    print(sum_num_list[e] - sum_num_list[s-1])