n = int(input())
s = 0

for i in range(1,n+1):
    
    if len(str(i)) <= 2:
        s+= 1
    else:
        digit = []
        for j in range(len(str(i))):
            digit.append(int(str(i)[j]))
        diff = digit[1]-digit[0]
        
        for i in range(2, len(digit)+1):
            if digit[i-1] != digit[i-2] + diff:
                break
            else:
                if i == len(digit):
                    s+= 1
print(s)