x, y = map(int, input().split())

answer = x + y + (min(x, y) // 10)

print(answer)