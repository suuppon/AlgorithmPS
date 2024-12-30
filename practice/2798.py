n, m = map(int, input().split())

cards = list(map(int, input().split()))

from itertools import combinations

comb = list(combinations(cards, 3))
d = 400000
for item in comb:
    if m - sum(item) >= 0 and m-sum(item) <= d:
        d = m - sum(item)

print(m-d) 