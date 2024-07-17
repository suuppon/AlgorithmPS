def make_table(score_table):
    dp_table = [0 for _ in range(len(score_table))]
    
    if len(score_table) == 1:
        return score_table[-1]
    elif len(score_table) == 2:
        return score_table[0] + score_table[1]
    elif len(score_table) == 3:
        return max(score_table[0] + score_table[2], score_table[1] + score_table[2])
    
    dp_table[0] = score_table[0]
    dp_table[1] = score_table[0] + score_table[1]
    dp_table[2] = max(score_table[0] + score_table[2], score_table[1] + score_table[2])
    
    for i in range(3, len(score_table)):
        dp_table[i] = max(dp_table[i-3] + score_table[i-1] + score_table[i], 
                          dp_table[i-2] + score_table[i]) 
        
    return dp_table[-1]

n = int(input())
score_table = []
for _ in range(n):
    score = int(input())
    
    score_table.append(score)
    
print(make_table(score_table=score_table))