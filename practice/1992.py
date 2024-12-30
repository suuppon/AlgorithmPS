import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def QuadTree(List, length):
    s = 0
    for l in List:
        s += sum(l)
        
    if s == length ** 2:
        return '1'
    if s == 0:
        return '0'
    
    half = length // 2
    result = '('
    result += QuadTree([l[:half] for l in List[:half]], half)
    result += QuadTree([l[half:] for l in List[:half]], half)
    result += QuadTree([l[:half] for l in List[half:]], half)
    result += QuadTree([l[half:] for l in List[half:]], half)
    result += ')'
    
    return result

N = int(input().rstrip())

QuadTreeList = []

for _ in range(N):
    l = list(map(int, input().split()))
    QuadTreeList.append(l)
    
print(QuadTree(QuadTreeList, N))

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def QuadTree(List, x, y, length):
    s = 0
    for i in range(x, x + length):
        s += sum(List[i][y:y + length])
    
    # 모든 원소가 1이면 '1' 반환
    if s == length ** 2:
        return '1'
    # 모든 원소가 0이면 '0' 반환
    if s == 0:
        return '0'
    
    # 리스트를 네 개로 분할하여 재귀적으로 처리
    half = length // 2
    result = '('
    # 왼쪽 위
    result += QuadTree(List, x, y, half)
    # 오른쪽 위
    result += QuadTree(List, x, y + half, half)
    # 왼쪽 아래
    result += QuadTree(List, x + half, y, half)
    # 오른쪽 아래
    result += QuadTree(List, x + half, y + half, half)
    result += ')'
    
    return result

# 입력 크기
N = int(input().rstrip())

# 쿼드 트리로 변환할 리스트 생성
QuadTreeList = []
for _ in range(N):
    l = list(map(int, input().strip()))
    QuadTreeList.append(l)
    
# 쿼드 트리 결과 출력
print(QuadTree(QuadTreeList, 0, 0, N))