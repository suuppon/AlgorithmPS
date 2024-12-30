import sys
input = sys.stdin.readline

string = input().strip()
sep_set = {'<', '>', '&&', '||', '(', ')'}

tmp = ''
token_list = []

i = 0
while i < len(string):
    if i < len(string) - 1 and string[i:i+2] in sep_set:
        if tmp:
            token_list.append(tmp)
            tmp = ''
        token_list.append(string[i:i+2])  # 2글자 구분자 추가
        i += 2
    # 1글자 구분자 처리
    elif string[i] in sep_set:
        if tmp:
            token_list.append(tmp)
            tmp = ''
        token_list.append(string[i])
        i += 1
    # 공백 처리
    elif string[i] == ' ':
        if tmp:
            token_list.append(tmp)
            tmp = ''
        i += 1
    # 일반 문자 처리
    else:
        tmp += string[i]
        i += 1

# 마지막 남은 문자열 처리
if tmp:
    token_list.append(tmp)

# 결과 문자열 생성
print(' '.join(token_list))