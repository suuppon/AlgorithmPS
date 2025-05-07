N,M = map(int, input().split())

#M번의 명령 수 받아서 명령들을 List에 저장
order = list(tuple(map(int, input().split())) for _ in range(M))

#원소가 모두 0인 N by 20 데이터프레임 생성해 기차 표현
df = [[0 for _ in range(20)] for _ in range(N)]

#명령 실행
for j in range(M):
    if order[j][0] == 1:
        df[order[j][1]-1][order[j][2]-1] = 1
    elif order[j][0] == 2:
        df[order[j][1]-1][order[j][2]-1] = 0
    elif order[j][0] == 3:
        df[order[j][1]-1].insert(0,0)
        df[order[j][1]-1].pop(-1)
    else:
        df[order[j][1]-1].pop(0)
        df[order[j][1]-1].append(0)

# 결과를 저장할 빈 집합 생성
my_set = set()

# 리스트 내의 각 리스트를 검사하여 집합에 추가
for sublist in df:
    # 리스트가 모두 0으로 이루어져 있지 않은 경우에만 집합에 추가
    my_set.add(tuple(sublist))

# 결과 확인
print(len(my_set))