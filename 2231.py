from itertools import combinations

n = int(input())



for i in range(n):
    k = 0
    k += i
    i = str(i)
    for num in i:
        k += int(num)
    if k == n:
        print(i)
        break
    if int(i) == n-1:
        print(0)

