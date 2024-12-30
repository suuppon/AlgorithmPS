n, d, k, c = map(int,input().split())

main_list = list()

for _ in range(n):
    x = int(input())
    main_list.append(x)

max_return = 0

for i in range(n):
    eat_sushi = 1
    sushi_list = [0 for _ in range(d+1)]
    sushi_list[c] = 1
                               
    for j in range(k):
        item = main_list[(i+j)%n]
        if sushi_list[item] == 0:
            sushi_list[item] = 1
            eat_sushi += 1
    max_return = max(eat_sushi, max_return)

print(max_return)