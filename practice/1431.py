n = int(input())

List = []

for _ in range(n):
    cereal = input()
    List.append(cereal)
    

def compare_length(c):
    return len(c)

def sum_of_digits(c):
    s = 0
    for char in c:
        try:
            num = int(char)
            s += num
        except:
            pass
        
    return s


List.sort(key=lambda x : (len(x), 
                          sum_of_digits(x), 
                          x))

for item in List:
    print(item)