n,m = map(int, input().split())

List_1 = list()
List_2 = list()

for i in range(n):
    row = list(map(int, input().split()))
    List_1.append(row)

for j in range(n):
    row = list(map(int, input().split()))
    List_2.append(row)

for i in range(len(List_1)):
    for j in range(len(List_1[0])):
            List_2[i][j] += List_1[i][j]

for row in List_2:
    for elt in row:
        print(elt, end=" ")
    print()