n = int(input())
num_list = list(map(int, input().split()))

check_table = [0 for _ in range(n)]

def main():
    cnt = 0
    
    for i in range(1, n):
        if num_list[i-1] > num_list[i]:
            check_table[i] = 1
            target_idx = i-1
            if num_list[i-2] > num_list[i]:
                return 0
    
    if sum(check_table) > 1:
        return 0
    if sum(check_table) == 0:
        return n
    
    for j in range(target_idx+1, n):
        if num_list[target_idx-1] <= num_list[j]:
            cnt += 1
        else:
            break
    return cnt

print(main())
