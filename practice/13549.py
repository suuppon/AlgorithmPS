

graph = [list() for _ in range(100001)]

for i in range(100000):
    graph[i].append((i+1, 1))
    graph[i+1].append((i, 1))
for i in range(1, 50000):
    graph[i].append((2*i, 1))

