N, S = map(int, input().split())
sequence = list(map(int, input().split()))
sequence.sort()

count = [0]

def backtrack(idx, current_sum):
    if idx >= N:
        return

    current_sum += sequence[idx]

    if current_sum == S:
        count[0] += 1

    # 현재 원소 포함 O
    backtrack(idx + 1, current_sum)
    # 현재 원소 미포함 X
    backtrack(idx + 1, current_sum - sequence[idx])  # 다시 빼줘야 원상복구됨

backtrack(0, 0)
print(count[0])