T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) #N*N 배열, M*M 파리채
    flies = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0

    for r in range(N-M+1):
        for c in range(N-M+1):
            dead_fly = 0
            # 파리채 크기만큼 진행하면서 죽인 파리 수 더해주기
            for i in range(M):
                for j in range(M):
                    dead_fly += flies[r+i][c+j]
            # 죽인 파리 최댓값 갱신
            max_kill = max(dead_fly, max_kill)
    
    print(f'#{tc} {max_kill}')
