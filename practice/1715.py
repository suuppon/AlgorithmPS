import heapq

# 입력 받기
n = int(input())
card_list = [int(input()) for _ in range(n)]

heapq.heapify(card_list)

total_cost = 0

while len(card_list) > 1:
    first = heapq.heappop(card_list)
    second = heapq.heappop(card_list)
    
    total_cost += first + second
    heapq.heappush(card_list, first+second)
    
print(total_cost)