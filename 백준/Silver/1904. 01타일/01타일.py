n = int(input())

prev_prev = 1
prev = 2

for i in range(3, n+1):
    answer = (prev + prev_prev) % 15746
    prev_prev = prev
    prev = answer

if n == 1:
    answer = 1
elif n == 2:
    answer = 2
    
print(answer % 15746)