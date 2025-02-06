n = int(input())

segment_list = list()

for _ in range(n):
    x, y = map(int, input().split())
    if len(segment_list) == 0:
        segment_list.append((x,y))
        continue
    
    for item in segment_list:
        if (item[0] >= x and item[0] <= y):
            item[0] = x
        elif (item[1] >= x and item[1] <= y):
            item[1] = y
        elif (item[0] >= x and item[1] <= y):
            item[0] = x
            item[1] = y
        