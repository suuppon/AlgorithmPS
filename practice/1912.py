import sys
input = sys.stdin.readline

def max_continuous_sum(sequence):
    sum1 = sequence[0]
    sum2 = sequence[1]
    
    for i in range(1, len(sequence)):
        if sum1 > 

def main():
    n = int(input())
    
    sequence = list(map(int, input().split()))
    print(max_continuous_sum(sequence))