n, k = map(int, input().split())
height_list = list(map(int, input().split()))

d_height_list = list()

for i in range(n-1):
    d_height_list.append(height_list[i+1] - height_list[i])
    
d_height_list.sort()

print(sum(d_height_list[:n-k]))