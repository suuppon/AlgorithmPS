import sys
input = sys.stdin.readline


def make_triangle_table(int_triangle):
    if len(int_triangle) == 1:
        return int_triangle
    
    dp_table = [[0]*i for i in range(1, len(int_triangle)+1)]
    
    dp_table[0][0] = int_triangle[0][0]
    
    for i in range(len(int_triangle)):
        for j in range(len(int_triangle[i])):
            if j == 0:
                dp_table[i][j] = dp_table[i-1][j] + int_triangle[i][j]
            elif j == len(int_triangle[i])-1:
                dp_table[i][j] = dp_table[i-1][j-1] + int_triangle[i][j]
            else:
                dp_table[i][j] = max(dp_table[i-1][j-1] + int_triangle[i][j], dp_table[i-1][j] + int_triangle[i][j])
                
    return dp_table
    
def main():
    n = int(input())

    int_triangle = list()
    
    for _ in range(n):
        nums = list(map(int, input().split()))
        int_triangle.append(nums)
    
    table = make_triangle_table(int_triangle)
    
    answer = max(table[-1])
    
    return answer

print(main())