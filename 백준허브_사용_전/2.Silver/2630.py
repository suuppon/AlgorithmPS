import sys
input = sys.stdin.readline

N = int(input())
paper = []

for _ in range(N):
    nums = list(map(int, input().split()))
    paper.append(nums)

result = list()
def solution(x, y, N):
    color = paper[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                return None

            
    if color == 0:
        result.append(0)
    elif color == 1:
        result.append(1)

solution(0,0,N)
print(result.count(0))
print(result.count(1))