def PrimeCheck(num):
    if num ==1:
        return 0
    
    if num == 2:
        return 1
    
    else:
        for i in range(2,num):
            if num % i != 0:
                pass
            else:
                return 0
            if i == num-1:
                return 1


_ = int(input())

num_list = list(map(int,input().split()))

c = 0

for num in num_list:
    c += PrimeCheck(num)

print(c)