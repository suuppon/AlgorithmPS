T = int(input())

def main():
    k = int(input())
    page_list = list(map(int, input().split()))
    
    page_list.sort()
    
    tmp_sum = page_list[0]
    summation = 0
    for i in range(1, k):
        tmp_sum += page_list[i]
        summation += tmp_sum
    
    print(summation)

for _ in range(T):
    main()