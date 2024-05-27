def DictReturn(matrix, Dict = {-1:0, 0:0, 1:0}):
    if len(matrix) == 1:
        Dict[matrix[0][0]] += 1
    else:
        sep = int(len(matrix)/3)
        List1 = matrix[0][0,sep] + matrix[0,sep][]