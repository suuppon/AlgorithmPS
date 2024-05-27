import sys
input = sys.stdin.readline

n = int(input())

dic = dict()
name_pairs = list()

for _ in range(n):
    name1, name2 = map(str, input().split())
    
    name_pairs.append((name1, name2))

for name_pair in name_pairs:
    dic[name_pair[0]] = 0
    dic[name_pair[1]] = 0

dic['ChongChong'] = 1

for name_pair in name_pairs:
    if dic[name_pair[0]] ==1 or dic[name_pair[1]] ==1:
        dic[name_pair[0]] = 1
        dic[name_pair[1]] = 1

print(sum(dic.values()))
