import sys
input = sys.stdin.readline

T = int(input())

def test():
    N = int(input())
    
    arr = list(tuple(map(int, input().split())) for _ in range(N))
    
    arr.sort()
    
    arr_2 = list(arr[i][1] for i in range(N))
    
    # 한 분야에서 1등은 무조건 포함시키기 때문에, count 1부터 시작
    cnt = 0
    
    top_rank = N+1
    
    for i in range(0, N):
        if arr_2[i] < top_rank:
            cnt += 1
            top_rank = arr_2[i]
            
    print(cnt)

for _ in range(T):
    test()