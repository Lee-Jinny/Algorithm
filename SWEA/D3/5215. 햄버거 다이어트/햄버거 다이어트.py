def ingredients(r, calorie, score):
    global max_score
    # 가지치기 : 칼로리가 제한을 초과
    if calorie >= L:
        return

    # 기저 조건
    if r == N:  # 모든 재료 고려
        max_score = max(score, max_score)
        return


    # 재귀 함수
    # 주어진 칼로리 이하 조합 중에서 가장 선호하는 조합
    if r < N:
        # 현재 재료를 선택
        ingredients(r + 1, calorie + evaluation[r][1], score + evaluation[r][0])

        # 현재 재료를 선택하지 않는 경우
        ingredients(r + 1, calorie, score)


T = int(input())


for tc in range(1, T+1):
    N, L = map(int, input().split())  # N : 재료의 수, L : 제한 칼로리
    evaluation =[list(map(int, input().split())) for _ in range(N)]
    max_score = 0

    ingredients(0, 0, 0)
    
    print(f'#{tc} {max_score}')


