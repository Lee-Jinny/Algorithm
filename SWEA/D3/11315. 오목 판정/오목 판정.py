def check_omok(N, omok):
    # 방향 벡터 (우, 하, 우하, 좌하)
    dr = [0, 1, 1, 1]
    dc = [1, 0, 1, -1]

    for r in range(N):
        for c in range(N):
            # 돌이 있을 때만 탐색
            if omok[r][c] == 'o':
                for d in range(4):  # 방향 4개 탐색
                    nr, nc = r, c
                    cnt = 0
                    # 현재 방향으로 5칸까지 연속 확인
                    while 0 <= nr < N and 0 <= nc < N and omok[nr][nc] == 'o':
                        cnt += 1
                        if cnt == 5:
                            return 'YES'
                        nr = nr + dr[d]
                        nc = nc + dc[d]  
    return 'NO'

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    omok = [list(input()) for _ in range(N)]  
    answer = check_omok(N, omok)
    print(f'#{tc} {answer}')
