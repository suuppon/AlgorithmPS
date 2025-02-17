n, h = map(int, input().split())

obstacles = [[False for _ in range(h)] for _i in range(n)]

for i in range(h):
    obstacle = int(input())

    if i % 2 == 0:
        for j in range(obstacle):
            obstacles[i][j] = True
    
    else:
        for j in range(obstacle):
            obstacles[i][h-1-j] = True
        
print(obstacles)

start = 0
end = n

visited = [False for _ in range(n+1)]

