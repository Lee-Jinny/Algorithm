T = int(input())  # 테스트 케이스 수 입력

# + 방향 벡터 (상, 하, 좌, 우)
dr_plus = [0, 1, 0, -1]
dc_plus = [1, 0, -1, 0]

# x 방향 벡터 (대각선 방향)
dr_cross = [1, 1, -1, -1]
dc_cross = [1, -1, -1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 배열 크기, M: 분사 범위
    arr = [list(map(int, input().split())) for _ in range(N)]  # N x N 배열 입력

    max_kill = 0  # 최대 죽인 수 초기화

    # 모든 칸에서 + 형태와 x 형태로 분사 시뮬레이션
    for r in range(N):
        for c in range(N):
            kill_plus = arr[r][c]  # + 방향으로 죽인 수
            kill_x = arr[r][c]     # x 방향으로 죽인 수

            # 4방향에 대해 M-1만큼의 범위 체크 (자기 자신 칸 제외)
            for d in range(4):
                for i in range(1, M):
                    # + 방향 이동
                    nr = r + dr_plus[d] * i
                    nc = c + dc_plus[d] * i

                    # x 방향 이동 (대각선)
                    ni = r + dr_cross[d] * i
                    nj = c + dc_cross[d] * i

                    # 배열의 범위 안에 있는지 확인 후 더하기
                    if 0 <= nr < N and 0 <= nc < N:
                        kill_plus += arr[nr][nc]
                    if 0 <= ni < N and 0 <= nj < N:
                        kill_x += arr[ni][nj]

            # 최대 죽인 수 갱신
            max_kill = max(kill_plus, kill_x, max_kill)

    # 테스트 케이스 결과 출력
    print(f'#{tc} {max_kill}')
