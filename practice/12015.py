n = int(input())
seq = list(map(int, input().split()))

start = 1
end = n

while start <= end:
    mid = (start + end) // 2
    
    