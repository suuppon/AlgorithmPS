N, S, M = map(int, input().split())

V = list(map(int, input().split()))

def valid(x):
    return 0 <= x <= M


dp_table = {S}

impossible = False

for i in range(N):
    v_cur = V[i]
    dp_table_new = set()
    for v_prev in dp_table:
        if valid(v_prev+v_cur):
            dp_table_new.add(v_prev+v_cur)
        if valid(v_prev-v_cur):
            dp_table_new.add(v_prev-v_cur)
    
    if len(dp_table_new) == 0:
        impossible = True
        break
    
    if i != N-1:
        dp_table = dp_table_new

if impossible:
    print(-1)
else:
    answer = max(dp_table_new)
    print(answer)