import sys
input = sys.stdin.readline

n, m = map(int, input().split())

word_dic = dict()

for _ in range(n):
    word = input().rstrip()

    if len(word) >= m:
        if word in word_dic.keys():
            word_dic[word] += 1
        else:
            word_dic[word] = 1

new_list = sorted(word_dic.keys(), key=lambda x: (-word_dic[x],-len(x), x ))

for word in new_list:
    print(word)