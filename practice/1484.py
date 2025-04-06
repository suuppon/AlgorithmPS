G = int(input())

arr = [i for i in range(50001)]

answer_list = []

start = 1
end = 2

while True:
    if end > 50000:
        break
    square_dif = arr[end]**2 - arr[start]**2
    
    if square_dif >= G:
        if square_dif == G:
            answer_list.append(end)
        start += 1
    else:
        end += 1 

if answer_list:
    for a in answer_list:
        print(a)
else:
    print(-1)

