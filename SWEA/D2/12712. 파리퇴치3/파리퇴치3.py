T = int(input())
          # 우, 하, 좌, 상
dr_plus = [0, 1, 0, -1]
dc_plus = [1, 0, -1, 0]
      # 우하, 좌하, 좌상, 우상
dr_x = [1, 1, -1, -1]
dc_x = [1, -1, -1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N: 배열의 크기 M: 스프레이 분사 크기

    flies= [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0

    # + 형태로 분사
    for r in range(N):
        for c in range(N):
            kill_plus = flies[r][c]
            kill_x = flies[r][c]

            # 4방향에 대해 체크
            for d in range(4):
                for i in range(1, M): # m 만큼 분사
                    # + 방향 이동
                    nr = r + dr_plus[d] * i
                    nc = c + dc_plus[d] * i

                    # x 방향 이동
                    ni = r + dr_x[d] * i
                    nj = c + dc_x[d] * i

                    # 배열의 범위 안에 있다면 값을 더해주기
                    if 0 <= nr < N and 0 <= nc < N:
                        kill_plus += flies[nr][nc]

                    if 0 <= ni < N and 0 <= nj < N:
                        kill_x += flies[ni][nj]

            # 최댓값 갱신
            max_kill = max(max_kill, kill_plus, kill_x)


    print(f'#{tc} {max_kill}')

