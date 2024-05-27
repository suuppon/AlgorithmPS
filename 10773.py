import sys
input = sys.stdin.readline

K = int(input())

num_list = [0]

for _ in range(K):
    num = int(input())

    if num == 0:
        pop = num_list.pop()
    else:
        num_list.append(num)

print(sum(num_list))