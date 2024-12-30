exp = input()

tmp = ''
tmp_num_list = []
num_list = []

for i in range(len(exp)):
    if i == len(exp) - 1:
        tmp += exp[i]
        tmp_num = int(tmp)
        tmp_num_list.append(tmp_num)
        num_list.append(sum(tmp_num_list))
    
    if exp[i] == '-':
        tmp_num = int(tmp)
        tmp_num_list.append(tmp_num)
        num_list.append(sum(tmp_num_list))
        tmp_num_list = []
        tmp = ''
        
    elif exp[i] == '+':
        tmp_num = int(tmp)
        tmp_num_list.append(tmp_num)
        tmp = ''
        
    else:
        tmp += exp[i]
        

answer = num_list[0]

if len(num_list) == 1:
    pass
else:
    for j in range(1, len(num_list)):
        answer -= num_list[j]
        
print(answer)