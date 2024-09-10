# 경로 압축을 적용하여 x의 대표자를 찾는 함수
def find(x):
    if P[x] == x:  # x가 자기 자신이면, 이는 대표자임을 의미
        return x
 
    # 경로 압축
    P[x] = find(P[x])  
    return P[x]
 
# 두 사람 x, y가 속한 집합을 합치는 함수 (union by rank)
def union(x, y):
    rootX = find(x)  # x의 대표자를 찾음
    rootY = find(y)  # y의 대표자를 찾음
 
    # 대표자가 다를 경우에만 합집합 연산을 수행
    if rootX != rootY:
        # rootX의 랭크가 더 크면 rootY를 rootX에 병합
        if rank[rootX] > rank[rootY]:
            P[rootY] = rootX
        # rootY의 랭크가 더 크면 rootX를 rootY에 병합
        elif rank[rootY] > rank[rootX]:
            P[rootX] = rootY
        # 랭크가 같으면 rootY를 rootX에 병합하고 rootX의 랭크를 1 증가
        else:
            P[rootY] = rootX
            rank[rootX] += 1
 
# 테스트 케이스 수 입력
T = int(input())
 
# 테스트 케이스 처리
for tc in range(1, T + 1):
    # N: 사람의 수, M: 서로 아는 관계의 수
    N, M = map(int, input().split())
     
    # 초기에는 모든 사람이 자기 자신을 대표자로 가짐
    P = [i for i in range(N + 1)]
    # 모든 집합의 초기 랭크는 1로 설정
    rank = [1] * (N + 1)
 
    # M개의 서로 아는 관계를 처리 (union 연산)
    for _ in range(M):
        fst, snd = map(int, input().split())
        union(fst, snd)
 
    # 무리의 개수를 셈 (고유한 대표자를 찾아 카운트)
    result = set()  # 중복된 대표자를 제외하기 위해 set 사용
    for i in range(1, N + 1):
        result.add(find(i))  # i번째 사람의 대표자를 찾아 set에 추가
     
    # 테스트 케이스 번호와 무리의 개수를 출력
    print(f'#{tc} {len(result)}')