from math import sin
a, b, c = map(int, input().split())

start = 0
end = c * 2

tol = 10**(-9)

def f(x):
    return a*x + b*sin(x) - c

answer = 0
while abs(end - start) >= tol:
    mid = (end + start) / 2
    
    if f(mid) >= 0:
        answer = mid
        end = mid    
    else:
        start = mid
    
print(answer)