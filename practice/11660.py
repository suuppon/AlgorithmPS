import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num_list = [[0] * (n+1)]

for _ in range(n):
    nums = [0] + list(map(int, input().split()))
    num_list.append(nums)

sum_list = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        sum_list[i][j] = num_list[i][j]
        sum_list[i][j] += sum_list[i-1][j] + sum_list[i][j-1] - sum_list[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = sum_list[x2][y2] - sum_list[x1-1][y2] - sum_list[x2][y1-1] + sum_list[x1-1][y1-1]
    print(answer)