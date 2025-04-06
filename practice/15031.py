import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())

num_students_wo_idx = list(map(int, input().split()))
capacity_of_buildings = list(map(int, input().split()))
yearly_rental_costs = list(map(int, input().split()))

building_list = list()
num_students = list()

for i in range(m):
    building_list.append((capacity_of_buildings[i], yearly_rental_costs[i], i+1))

for i in range(n):
    num_students.append((num_students_wo_idx[i], i)) 

num_students.sort(reverse=True)

def main():
    finished = False
    answer = list()
    visited_set = set()
    
    for i in range(n):
        finished = False
        building_list.sort(key=lambda x: x[1])
        for j in range(m):
            elt = building_list[j]
            
            if elt[0] >= num_students[i][0] and elt not in visited_set:
                answer.append([elt[2], num_students[i][1]])
                visited_set.add(elt)
                finished = True
                break
            
            if j == m-1 and not finished:
                print('impossible')
                return None
        
    answer.sort(key=lambda x: x[1])
    
    for item in answer:
        print(item[0], end=' ')

main()