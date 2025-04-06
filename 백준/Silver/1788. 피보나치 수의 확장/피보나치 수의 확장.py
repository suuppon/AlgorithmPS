n = int(input())

if n == 0:
    answer = 0
elif n == 1:
    answer = 1
elif n > 1:
    prev_prev = 0 #f(0)
    prev = 1 #f(1)
    
    for _ in range(n-1):
        answer = prev_prev + prev #f(n) = f(n-2) + f(n-1)
        prev_prev = prev
        prev = answer
else:
    prev_prev = 1 #f(1)
    prev = 0 #f(0)
    for _ in range(-n):
        answer = prev_prev - prev #f(n-2) = f(n) - f(n-1)
        prev_prev = prev
        prev = answer
        
if answer < 0:
    sign = -1
elif answer > 0:
    sign = 1
else:
    sign = 0

print(sign)
print((sign * answer) % 1000000000)