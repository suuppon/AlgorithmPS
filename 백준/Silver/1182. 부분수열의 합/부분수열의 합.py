N, S = map(int, input().split())
sequence = list(map(int, input().split()))
sequence.sort()

count = 0

def backtrack(idx, current_sum):
    global count
    if idx >= N:
        return

    current_sum += sequence[idx]

    if current_sum == S:
        count += 1
        
    backtrack(idx + 1, current_sum)
    backtrack(idx + 1, current_sum - sequence[idx])

backtrack(0, 0)
print(count)