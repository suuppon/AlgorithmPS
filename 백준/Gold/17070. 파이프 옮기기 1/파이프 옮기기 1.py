
N = int(input())
house = list()

default_dict = {'horizontal': 0,
                'vertical': 0,
                'diagonal': 0}

def index_val(idx):
    x, y = idx
    if 0<=x<N and 0<=y<N:
        return True
    else:
        return False
    
for _ in range(N):
    row = list(map(int, input().split()))
    house.append(row)

dp = [[default_dict.copy() for _ in range(N)] for _ in range(N)]

dp[0][1]['horizontal'] = 1

for i in range(N):
    for j in range(2, N):
        if house[i][j] ==1:
            continue
        
        if index_val((i-1, j)):
            dp[i][j]['vertical'] += dp[i-1][j]['diagonal'] + dp[i-1][j]['vertical']
        if index_val((i, j-1)):
            dp[i][j]['horizontal'] += dp[i][j-1]['diagonal'] + dp[i][j-1]['horizontal']
        if index_val((i-1, j-1)) and (1-house[i-1][j]) * (1-house[i][j-1]) != 0:
            dp[i][j]['diagonal'] += dp[i-1][j-1]['diagonal'] + dp[i-1][j-1]['horizontal'] + dp[i-1][j-1]['vertical']
        
                
print(sum(dp[N-1][N-1].values()))