import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
players = range(N)
min_diff = float('inf')

def calc_score(team):
    score = 0
    for i, j in combinations(team, 2):
        score += table[i][j] + table[j][i]
    return score

for start_team in combinations(players, N // 2):
    link_team = set(players) - set(start_team)
    start_score = calc_score(start_team)
    link_score = calc_score(link_team)
    min_diff = min(min_diff, abs(start_score - link_score))
    if min_diff == 0:
        break

print(min_diff)