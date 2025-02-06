def test():
    N = int(input())
    
    arr = list()
    for _ in range(N):
        p, s = map(int, input().split())
        arr.append([p, s])
    
T = int(input())

for i in range(T):
    result = test()
    
    print(f"Case #{i+1}: {result}")