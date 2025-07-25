import sys
input = sys.stdin.readline

INF = int(1e9)

N = int(input())
matrix = list(list(map(int, input().split())) for _ in range(N))

dp_table = [[INF for _ in range(3)] for _ in range(N)]
dp_table[0] = [matrix[0][0], matrix[0][1], matrix[0][2]]

for i in range(1, N):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp_table[i][j] = min(dp_table[i-1][k] + matrix[i][j], dp_table[i][j])
                
print(min(dp_table[-1]))