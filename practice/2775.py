T = int(input())

apartment = [[0 for _ in range(15)] for _ in range(15)]

for i in range(1, 15):
    apartment[0][i] = i

for i in range(1, 15):
    for j in range(1, 15):
        apartment[j][i] = sum(apartment[j-1][:i+1])

for _ in range(T):    
    k = int(input())
    n = int(input())
    print(apartment[k][n])
