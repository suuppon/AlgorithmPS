import sys
input = sys.stdin.readline
INF = int(1e9)


xs, ys = map(int, input().split())
xe, ye = map(int, input().split())

gate_list = list()

# 1 : start
# 2 : end
# 3 : gate 1 start
# 4 : gate 1 end
# 5 : gate 2 start
# 6 : gate 2 end
# 7 : gate 3 start
# 8 : gate 3 end
dp_table = [[INF for _ in range(9)] for _ in range(9)]

distance = abs(xs - xe) + abs(ys - ye)
dp_table[1][2] = distance
dp_table[2][1] = distance

gate_list = list()

for i in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    
    gate_list.append(((x1, y1), (x2, y2)))
    
for i in range(3):
    
    dp_table[2*i+3][2*i+4] = 10
    dp_table[2*i+4][2*i+3] = 10
    dp_table[2*i+3][1] = abs(gate_list[i][0][0] - xs) + abs(gate_list[i][0][1] - ys)
    dp_table[2*i+4][1] = abs(gate_list[i][1][0] - xs) + abs(gate_list[i][1][1] - ys)
    dp_table[2*i+3][2] = abs(gate_list[i][0][0] - xe) + abs(gate_list[i][0][1] - ye)
    dp_table[2*i+4][2] = abs(gate_list[i][1][0] - xe) + abs(gate_list[i][1][1] - ye)
    
    dp_table[1][2*i+3] = dp_table[2*i+3][1]
    dp_table[1][2*i+4] = dp_table[2*i+4][1]
    dp_table[2][2*i+3] = dp_table[2*i+3][2]
    dp_table[2][2*i+4] = dp_table[2*i+4][2]
    
    for j in range(3):
        if i != j:
            dp_table[2*i+3][2*j+3] = abs(gate_list[i][0][0] - gate_list[j][0][0]) + abs(gate_list[i][0][1] - gate_list[j][0][1])
            dp_table[2*j+3][2*i+3] = dp_table[2*i+3][2*j+3]
            
            dp_table[2*i+4][2*j+4] = abs(gate_list[i][1][0] - gate_list[j][1][0]) + abs(gate_list[i][1][1] - gate_list[j][1][1])
            dp_table[2*j+4][2*i+4] = dp_table[2*i+4][2*j+4]
            
            dp_table[2*i+3][2*j+4] = abs(gate_list[i][0][0] - gate_list[j][1][0]) + abs(gate_list[i][0][1] - gate_list[j][1][1])
            dp_table[2*j+4][2*i+3] = dp_table[2*i+3][2*j+4]
            
            dp_table[2*i+4][2*j+3] = abs(gate_list[i][1][0] - gate_list[j][0][0]) + abs(gate_list[i][1][1] - gate_list[j][0][1])
            dp_table[2*j+3][2*i+4] = dp_table[2*i+4][2*j+3]


for i in range(1, 9):
    dp_table[i][i] = 0
    

for k in range(1, 9):
    for i in range(1, 9):
        for j in range(1, 9):
            dp_table[i][j] = min(dp_table[i][k] + dp_table[k][j], dp_table[i][j])

print(dp_table[1][2])