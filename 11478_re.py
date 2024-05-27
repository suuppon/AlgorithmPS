import sys
input = sys.stdin.readline

S = input()

strings = set()

for i in range(len(S)):
    for j in range(i+1, len(S)):
        string = S[i:j]
        strings.add(string)

print(len(strings))