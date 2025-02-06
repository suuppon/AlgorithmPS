N = int(input())

def month_day_to_num_days(month, day):

    days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(days_list[:month - 1]) + day


arr = list()
all_dates_arr = list()

princess_start, princess_end = month_day_to_num_days(3, 1), month_day_to_num_days(11, 30)

for _ in range(N):
    start_month, start_day, end_month, end_day = map(int, input().split())
    start_day, end_day = month_day_to_num_days(start_month, start_day), month_day_to_num_days(end_month, end_day)
    
    all_dates_arr.append([start_day, end_day])
    if start_day <= princess_end and end_day >= princess_start:
        arr.append([start_day, end_day])
    else:
        continue


arr.sort(key = lambda x : x[0])