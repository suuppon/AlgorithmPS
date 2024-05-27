n, m = map(int, input().split())

set_1 = set(map(int, input().split()))
set_2 = set(map(int, input().split()))

sym_diff = set_1.symmetric_difference(set_2)

print(len(sym_diff))