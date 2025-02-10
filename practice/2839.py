N = int(input())

table = [-1] * 5001

table[3] = 1
table[5] = 1

for i in range(6, 5001):
    
    if table[i-3] == -1 and table[i-5] == -1:
        pass

    if table[i-3] != -1 and table[i-5] == -1:
        table[i] = table[i-3] + 1
    
    if table[i-5] != -1 and table[i-3] == -1:
        table[i] = table[i-5] + 1
        
    if table[i-5] != -1 and table[i-3] != -1:
        table[i] = min(table[i-3] + 1, table[i-5] + 1)
        
print(table[N])