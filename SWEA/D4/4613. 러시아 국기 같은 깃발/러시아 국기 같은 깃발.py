T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N*M
    flag = [input() for _ in range(N)]

    mx = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            cnt = 0
            for k in range(i + 1):
                cnt += flag[k].count('W')  # 하얀색 깃발 개수 count
            for k in range(i + 1, j + 1):
                cnt += flag[k].count('B')
            for k in range(j + 1, N):
                cnt += flag[k].count('R')
            mx = max(mx, cnt)
    print(f'#{tc} {N * M - mx}')

