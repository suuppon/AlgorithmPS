n,k = map(int, input().split())

num_list = list(map(int, input().split()))

total = 0

#Bubble sort
for i in range(0, n):
    for j in range(0, n-1-i):
        if num_list[j] < num_list[j+1]:
            tmp = num_list[j+1]
            num_list[j+1] = num_list[j]
            num_list[j] = tmp
        else:
            pass

cutline = num_list[k-1]

print(cutline)