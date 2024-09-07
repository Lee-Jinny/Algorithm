T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 농장 크기 N*N
    crops = [list(map(int, input())) for _ in range(N)]

    value = 0  # 농작물의 가치를 저장할 변수
    center = N//2 # 농장크기가 항상 홀 수 이므로 가운데는 N을 2로 나눈 몫으로 설정

    # 농장의 각 행을 순회하며, 중앙을 기준으로 대칭 범위인 농작물 가치를 합산
    for r in range(N):
        start = abs(center - r)
        end = N - start
        for c in range(start, end):
            value += crops[r][c]

    print(f'#{tc} {value}')
