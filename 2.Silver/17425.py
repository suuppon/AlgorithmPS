import sys
input = sys.stdin.readline

def prime_factor(n):
    factor_dict = dict()
    factor = 2
    while n >= factor:
        if n%factor == 0:
            if factor in factor_dict.keys():
                factor_dict[factor] += 1
            else:
                factor_dict[factor] = 1
            
            n = n//factor
        else:
            factor += 1
    return factor_dict

T = int(input())

for _ in range(T):
    N = int(input())
    factor_dict = prime_factor(N)
    answer = 1
    for key in factor_dict.keys():
        answer *= (key**(factor_dict[key]+1)-1)//(key-1)
    print(answer)