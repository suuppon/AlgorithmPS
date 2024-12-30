import sys
input = sys.stdin.readline

n, k = map(int, input().split())

num_list = list(map(int, input().split()))

sum_list = [sum(num_list[0:k])]

for i in range(1, n-k+1):
    sum_list.append(sum_list[i-1] - num_list[i-1] + num_list[i+k-1])
print(max(sum_list))