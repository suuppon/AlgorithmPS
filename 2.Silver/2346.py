import sys
input = sys.stdin.readline

n = int(input())

baloons = [i for i in range(1, n+1)]

nums = list(map(int, input().split()))

idx = 0

while len(baloons) > 0:
    idx = idx%len(baloons)
    x = baloons.pop(idx)
    print(x, end = ' ')
    paper_num = nums[x-1]
    if paper_num < 0:
        next_idx = (idx + paper_num)
    else:
        next_idx = (idx + paper_num - 1)
    idx = next_idx