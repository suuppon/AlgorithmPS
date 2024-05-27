N = int(input())

score_list = []

for _ in range(N):
    name, *score = map(str, input().split())
    score_list.append([name, *map(int,score)])

score_list.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for st in score_list:
    print(st[0])