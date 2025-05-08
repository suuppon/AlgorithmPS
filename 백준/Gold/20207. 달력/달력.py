import sys
input = sys.stdin.readline

N = int(input())

calendar = dict()
min_S, max_E = 366, -1

date_list = list()

for _ in range(N):
    S, E = map(int, input().split())
    min_S, max_E = min(S, min_S), max(E, max_E)
    date_list.append((S, E))

date_list.sort(key= lambda x : (x[0], -x[1]))

for day in range(min_S, max_E+1):
    calendar[day] = 0
    
for S, E in date_list:
    for day in range(S, E+1):
        if day in calendar.keys():
            calendar[day] += 1

calendar['last'] = 0

maximum, length, answer = 0, 0, 0

for key, value in calendar.items():
    
    if value == 0:
        answer += length * maximum
        length, maximum = 0, 0
        
    else:
        length += 1
        maximum = max(maximum, value)

print(answer)