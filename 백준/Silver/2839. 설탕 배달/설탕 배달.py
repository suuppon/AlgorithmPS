N = int(input())
p = 0
if N%5 == 0:
    print(int(N/5))
    
    
else:
    while True:
        N-= 3
        
        if N%5 == 0:
            p += 1
            print(int(p+N/5))
            break
        else:
            if N<0:
                print(-1)
                break
            else:
                p += 1