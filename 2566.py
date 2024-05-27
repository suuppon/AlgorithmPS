def FindMatrixMaximum(matrix):
    rowmaxdict = {}
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            row_max = max(matrix[i])
            if matrix[i][j] == row_max:
                rowmaxdict["{} {}".format(i+1, j+1)] =  matrix[i][j]

    max_value = max(rowmaxdict.values())

    for key in rowmaxdict.keys():
        if rowmaxdict[key] == max_value:
            max_key = key

    return(max_key, max_value)



matrix = []

for _ in range(9):
    row = list(map(int, input().split()))
    matrix.append(row)

key, value = FindMatrixMaximum(matrix=matrix)

print(value)
print(key)

