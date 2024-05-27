def Compute_i(X,Y,Z):
    if Z >= 99:
        return -1
    else:
        i = (X*Z+X-100*Y)//(99-Z)
        if i == int(i):
            return int(i)
        else:
            return int(i+1)


def Compute_index(X,Y,Z):
    i = Compute_i(X,Y,Z)
    if i == -1:
        return -1
    
    while True:
        if Z < int(((Y+i)/(X+i)*100)):
            break
        else:
            i += 1
    return i

X, Y = map(int, input().split())
Z = int(Y/X * 100)

i = Compute_index(X,Y,Z)

print(i)