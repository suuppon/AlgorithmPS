n = int(input())

num_list = list()

for _ in range(n):
    num = int(input())
    num_list.append(num)

for i in range(n-1):
    for j in range(n-i-1):
        if num_list[j+1] < num_list[j]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

for i in range(len(num_list)):
    print(num_list[i])