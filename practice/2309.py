from itertools import combinations

List = []

for _ in range(9):
    height = int(input())
    List.append(height)
    
combination_result = combinations(List, 7)

for elt in combination_result:
    if sum(elt) == 100:
        answer = list(elt)
        break

answer.sort()

for elt in answer:
    print(elt)