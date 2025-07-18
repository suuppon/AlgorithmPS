k = int(input())
n = int(input())
target = list(input())
ladder = [list(input()) for _ in range(n)]

question_row = 0
for i in range(n):
    if ladder[i][0] == '?':
        question_row = i
        break

def go_down(start_idx, until_row):
    pos = list(range(k))
    for i in range(until_row):
        for j in range(k-1):
            if ladder[i][j] == '-':
                pos[j], pos[j+1] = pos[j+1], pos[j]
    return pos

def go_up(start_idx, from_row):
    pos = list(range(k))
    for i in range(n-1, from_row, -1):
        for j in range(k-1):
            if ladder[i][j] == '-':
                pos[j], pos[j+1] = pos[j+1], pos[j]
    return pos

# top_state[i] : i번째 세로선의 원래 알파벳 index
# bottom_state[i] : i번째 세로선이 도달해야 하는 target의 index
top_state = go_down(0, question_row)
bottom_state = go_up(0, question_row)

# 최종 알파벳 index
target_index = [ord(c) - ord('A') for c in target]
bottom_state = [target_index[i] for i in bottom_state]

# 이제 top_state → bottom_state로 바꾸는 데 필요한 줄을 구성
result = ['*'] * (k-1)

for i in range(k-1):
    if top_state[i] == bottom_state[i]:
        continue
    elif top_state[i] == bottom_state[i+1] and top_state[i+1] == bottom_state[i]:
        # Swap 필요 → 가로 막대 필요
        result[i] = '-'
        # Swap 시키기
        top_state[i], top_state[i+1] = top_state[i+1], top_state[i]
    else:
        # 한 번의 swap으로 해결 불가
        print('x' * (k-1))
        break
else:
    print(''.join(result))