n = int(input())

i = 0

while True:
    if (i**2 + i)/2 < n:
        i+= 1
    else:
        break

if i%2 == 0:
    
    k = i-((i**2+i)/2-n)
    h = i+1-k
else:
    h = i-((i**2+i)/2-n)
    k = i+1-h
if n ==1:
    print("1/1")
else:
    print("%d/%d" %(k,h))
    