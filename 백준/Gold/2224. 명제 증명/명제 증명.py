import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())

dict_char_to_num = {chr(i): i - 64 for i in range(65, 91)}
dict_char_to_num.update({chr(i): i-70 for i in range(97, 123)})

dict_num_to_char = {v: k for k, v in dict_char_to_num.items()}

graph = [[INF for _ in range(52+1)] for _ in range(52+1)]

for i in range(1, 52+1):
    graph[i][i] = 0

for _ in range(n):
    prop = input().rstrip()
    p, q = prop.split(" => ")
    p_num, q_num = dict_char_to_num[p], dict_char_to_num[q]
    graph[p_num][q_num] = 1

for k in range(1, 52+1):
    for i in range(1, 52+1):
        for j in range(1, 52+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer_list = list()

for i in range(1, 52+1):
    for j in range(1, 52+1):
        if i != j and graph[i][j] < INF:
            p, q = dict_num_to_char[i], dict_num_to_char[j]
            answer_list.append((p, q))

length = len(answer_list)
print(length)
for p, q in answer_list:
    print(f"{p} => {q}")