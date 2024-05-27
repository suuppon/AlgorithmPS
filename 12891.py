import sys
input = sys.stdin.readline

s, p = map(int, input().split())
DNA_string = input().rstrip()
A, C, G, T = map(int, input().split())


def password_check(string):
    char_dict = {'A':0, 'T':0, 'C':0, 'G':0}
    for char in string:
        char_dict[char] += 1
    
    if char_dict['A'] >= A and char_dict['T'] >= T and char_dict['C'] >= C and char_dict['G'] >= G:
        return 1
    else:
        return 0
    
c = 0
for i in range(s-p+1):
    string = DNA_string[i:i+p]
    c += password_check(string)
print(c)