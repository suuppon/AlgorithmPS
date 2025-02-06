import heapq

n = int(input())

arr = list()

for _ in range(n):
    p, d = map(int, input().split())
    arr.append([p, d])
    
arr.sort(key = lambda x : x[-1])

cur_day = 0
heap = list()

for p, d in arr:
    heapq.heappush(heap, p)
    cur_day += 1
    
    if cur_day > d:
        heapq.heappop(heap)
        cur_day -= 1
        
print(sum(heap))