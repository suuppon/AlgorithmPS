import sys
input = sys.stdin.readline

n = int(input())

honey_list = list(map(int, input().split()))

sum_list = [0]
for i in range(1, n+1):
    sum_list.append(sum_list[i-1]+honey_list[i-1])

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if i == j or j == k or k == i:
                pass
            
            honey = i
            bee1 = j
            bee2 = k

            if bee1 < honey < bee2 or bee2 < honey < bee1:
                answer = 

