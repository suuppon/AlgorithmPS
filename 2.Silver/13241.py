a, b = map(int, input().split())

def Euclidean(a, b):
    while a != 0:
        [b, a] = [a, b%a]
    return b

gcd = Euclidean(min(a,b), max(a,b))

lcm = int(a*b/gcd)

print(lcm)