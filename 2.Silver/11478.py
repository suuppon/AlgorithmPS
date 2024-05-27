import sys

input = sys.stdin.readline

S = input().rstrip()

string_set = set()

for i in range(len(S)+1):
    for j in range(i+1, len(S)+1):
        string_set.add(S[i:j])

print(len(string_set))
