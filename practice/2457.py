from collections import deque

N = int(input())

def month_day_to_num_days(month, day):

    days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(days_list[:month - 1]) + day


arr = list()
all_dates_arr = list()

possibility_check = [0 for _ in range(366)]

start_border = month_day_to_num_days(3, 1)
end_border = month_day_to_num_days(11, 30)

for _ in range(N):
    start_month, start_day, end_month, end_day = map(int, input().split())
    start_day, end_day = month_day_to_num_days(start_month, start_day), month_day_to_num_days(end_month, end_day)
    
    all_dates_arr.append([start_day, end_day])
    
    for i in range(start_day, end_day + 1):
        possibility_check[i] = True
    
    if start_day <= end_border and end_day >= start_border:
        arr.append([start_day, end_day])
    else:
        continue

def main(arr):
    for i in range(start_border, end_border + 1):
        if possibility_check[i] == False:
            return 0
        
    end = 0
    cnt = 0
    prev_end = start_border
    while end < end_border:
        arr.sort(key = lambda x : -x[1])
        i = 0
        while arr:
            elt = arr[i]
            arr = list(arr)
            i += 1
            end_date = elt[1]
            start_date = elt[0]
            if prev_end <= end_date and start_date <= prev_end:
                arr = deque(arr)
                cnt += 1
                end = end_date
                _ = arr.popleft()
                arr = list(arr)
                break
    
    return cnt

print(main(arr))