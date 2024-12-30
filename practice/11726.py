def make_table():
    table = [0]*1001
    table[1] = 1
    table[2] = 2
    
    for i in range(3, 1001):
        table[i] = (table[i-1] + table[i-2]) % 10007
        
    return table

def main():
    n = int(input())
    table = make_table()
    
    print(table[n])
    
main()