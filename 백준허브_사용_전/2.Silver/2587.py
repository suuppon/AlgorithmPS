total = 0
num_list = [0]
for _ in range(5):
    num = int(input())
    num_list.append(num)
    total += num

mean = int(total/5)

for i in range(1, 6):
    for j in range(1, 6-i):
        if num_list[j] < num_list[j+1]:
            tmp = num_list[j+1]
            num_list[j+1] = num_list[j]
            num_list[j] = tmp
        else:
            pass

median = int(num_list[3])

print(mean)
print(median)