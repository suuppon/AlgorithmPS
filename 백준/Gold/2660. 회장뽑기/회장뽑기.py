from collections import deque

n = int(input())

table = [[] for _ in range(n+1)]

while True:
    a, b = map(int, input().split())
    table[a].append(b)
    table[b].append(a)
    
    if a == -1:
        break

def test(start):
    visited = [False for _ in range(n+1)]

    def bfs(start):
        score = 0
        queue = deque([[start, 0]])
        
        while len(queue) != 0:
            elt = queue.popleft()
            if not visited[elt[0]]: 
                score = max(elt[1], score)
                visited[elt[0]] = True
                for neighbor in table[elt[0]]:
                    queue.append([neighbor, elt[1]+1])
                    
        return score
    
    score = bfs(start)
    return score

score_list = []
for i in range(1, n+1):
    score = test(i)
    score_list.append(score)

minimum = min(score_list)
    
cand = []

for j in range(n):
    if score_list[j] == minimum:
        cand.append(j+1)
        
print(minimum, len(cand))
for c in cand:
    print(c, end=' ')