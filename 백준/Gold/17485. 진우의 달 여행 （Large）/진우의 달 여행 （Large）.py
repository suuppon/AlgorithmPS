import sys
input = sys.stdin.read

data = input().split()
N, M = map(int, data[:2])
matrix = [list(map(int, data[i * M + 2:(i + 1) * M + 2])) for i in range(N)]

INF = int(1e9)
dp = [[[INF]*3 for _ in range(M)] for _ in range(N)]

for j in range(M):
    for d in range(3):
        dp[0][j][d] = matrix[0][j]

for i in range(1, N):
    for j in range(M):
        for d in range(3):
            nj = j + (d - 1)
            if 0 <= nj < M:
                for pd in range(3):
                    if pd != d:
                        dp[i][j][d] = min(dp[i][j][d], dp[i-1][nj][pd] + matrix[i][j])

print(min(min(row) for row in dp[N-1]))