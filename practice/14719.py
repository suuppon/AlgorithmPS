import sys
input = sys.stdin.readline

h, w = map(int, input().split())
num_blocks = list(map(int, input().split()))

blocks = list()

for _ in range(h):
    row = list()
    for i in range(w):
        if num_blocks[i] > 0:
            num_blocks[i] -= 1
            row.append(1)
        else:
            row.append(0)
    
    blocks.append(row)

cnt = 0

for row in blocks:
    left, right = None, None
    for i in range(w):
        if row[i] == 1:
            left = i
            break
    for j in range(w):
        if row[w-1-j] == 1:
            right = w-1-j
            break
    
    if left == None or right == None or left == right:
        continue

    for i in range(left, right+1):
        if row[i] == 0:
            cnt += 1

print(cnt)