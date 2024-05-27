Dict = {}

for i in range(10):
    Dict[i] = "{}".format(i)
    
for i in range(ord('A'), ord('Z')+1):
    Dict[i - ord('A') + 10] = chr(i)


n, b = map(int, input().split())

remainder_list = []

if n ==0:
    remainder_list.append(n)
    
while n > 0:
    remainder_list.append(n % b)
    n = n // b


transformed_n = ""

for i in range(len(remainder_list)):
    transformed_n += Dict[remainder_list[-i-1]]


print(transformed_n)