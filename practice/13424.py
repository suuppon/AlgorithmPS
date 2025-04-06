import sys
input = sys.stdin.readline
INF = int(1e9)

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    
    graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        graph[i][i] = 0
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c
        
    k = int(input())
    room_num_list = list(map(int, input().split()))
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    minimum = INF
    target_room_num = 0
    
    for i in range(1, n+1):
        total_cost = sum(graph[i][r] for r in room_num_list)
        if total_cost < minimum:
            target_room_num = i
            minimum = total_cost
            
    print(target_room_num)