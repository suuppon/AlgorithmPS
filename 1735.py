a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

denominator = b1 * b2
numerator = a1*b2 + a2*b1

def Euclidean(a,b):
    while b != 0:
        (a, b) = (b, a%b)
    return a

gcd = Euclidean(max(denominator, numerator), min(denominator, numerator))

denominator1 = int(denominator/gcd)
numerator1 = int(numerator/gcd)

print(numerator1, denominator1)