N = int(input())
arr = list(map(int, input().split()))

dp_table = [1001] * N
dp_table[0] = 0  # 시작점은 0번 점프

for i in range(N):
    if dp_table[i] == 1001:
        continue  # 도달 못한 위치는 건너뜀
    for j in range(1, arr[i] + 1):
        if i + j < N:
            dp_table[i + j] = min(dp_table[i + j], dp_table[i] + 1)

answer = -1 if dp_table[N - 1] == 1001 else dp_table[N - 1]
print(answer)