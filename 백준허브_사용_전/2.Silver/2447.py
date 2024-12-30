import sys
input = sys.stdin.readline

def StarRecursion(n):
    if n == 1:
        star_list = ["*"]
        return star_list
    
    star_list = StarRecursion(n//3)
    List = []
    for star in star_list:
        List.append(star*3)
    for star in star_list:
        List.append(star+" "*(n//3)+star)
    for star in star_list:
        List.append(star*3)
    
    return List
    
n = int(input())

stars = StarRecursion(n)

for star in stars:
    print(star)