import sys
input = sys.stdin.readline

def make_table():
    table = [0]*1001
    table[1] = 1
    table[2] = 3
    
    for i in range(3, 1001):
        table[i] = (table[i-1] + 2 * table[i-2]) % 10007
        
    return table


def main():
    n = int(input())

    print(make_table()[n] % 10007)

main()