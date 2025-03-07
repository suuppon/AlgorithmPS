from collections import deque

F, S, G, U, D = map(int, input().split())

def bfs():
    check = [0 for _ in range(F+1)]

    check[S] = 1

    queue = deque([S])
    while queue:
        elt = queue.popleft()
        
        if elt == G:
            return check[G] - 1
        else:
            for new in (elt + U, elt - D):
                if 0 < new <= F and check[new] == 0:
                    queue.append(new)
                    check[new] = check[elt] + 1
    
    return 'use the stairs'

print(bfs())