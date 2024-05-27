import sys
input = sys.stdin.readline

def open_and_close(window):
    return 1-window

n = int(input())

windows = [0 for _ in range(n+1)]


for i in range(1, n+1):
    ith = i
    tmp = ith
    while ith <= n:
        windows[ith] = open_and_close(windows[ith])
        ith += tmp

print(sum(windows))