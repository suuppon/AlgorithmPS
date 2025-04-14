import sys
input = sys.stdin.readline

N = int(input())

num_list = list(map(str, input().split()))

num_len_dict = {}

for n in num_list:
    length = len(n)
    if length not in num_len_dict.keys():
        num_len_dict[length] = [int(n)]
    else:
        num_len_dict[length].append(int(n))
        
