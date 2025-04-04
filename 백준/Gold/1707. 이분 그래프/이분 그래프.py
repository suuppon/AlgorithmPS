import sys
input = sys.stdin.readline
from collections import deque

def is_bipartite(V, graph):
    color = [None] * (V + 1)  # None: 아직 색칠 안됨, 0 또는 1로 색칠됨

    for start in range(1, V + 1):
        if color[start] is None:
            queue = deque([start])
            color[start] = 0

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] is None:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False  # 인접한 노드끼리 같은 색이면 이분 그래프 아님
    return True

k = int(input())

for _ in range(k):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    answer = "YES" if is_bipartite(V, graph) else "NO"
    print(answer)