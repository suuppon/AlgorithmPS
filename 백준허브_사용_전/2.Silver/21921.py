import sys
input = sys.stdin.readline

n, x = map(int, input().split())

visitors_list = list(map(int, input().split()))

sliding_window = [0] * (n-x+2)

sliding_window[1] = sum(visitors_list[0:x])

for i in range(2, n-x+2):
    sliding_window[i] = sliding_window[i-1] + visitors_list[i+x-2] - visitors_list[i-2]

answer = max(sliding_window)

if answer == 0:
    print('SAD')
else:
    c = sliding_window.count(answer)
    print(answer)
    print(c)