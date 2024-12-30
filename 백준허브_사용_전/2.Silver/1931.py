import sys
input = sys.stdin.readline

n = int(input())

time_list = []

for _ in range(n):
    t1, t2 = map(int, input().split())
    time_list.append((t1, t2))

time_list.sort(key=lambda x: [x[1], x[0]])

c = 1
time = time_list[0]

for i in range(1, n):
    if time[1] <= time_list[i][0]:
        c += 1
        time = time_list[i]
    else:
        pass

print(c)