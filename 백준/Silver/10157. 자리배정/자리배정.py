C, R = map(int, input().split())  # 가로로 C개, 세로로 R개의 좌석이 C×R 격자형

K = int(input()) # 찾을 번호
     # 상, 우, 하, 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

seat = [[0]* C for _ in range(R)]

d = 0 # 시작 방향은 왼쪽
r, c = R-1, 0 # 시작 위치는 좌측 하단

for i in range(1, C * R +1):
    seat[r][c] = i

    if i == K:
        print(c+1, R-r)
        break

    # 다음 위치 계산
    nr = r + dr[d]
    nc = c + dc[d]

    # 경계 또는 이미 채워진 좌석일 경우 방향 전환
    if nr < 0 or nr >= R or nc < 0 or nc >= C or seat[nr][nc] != 0:
        d = (d + 1) % 4  # 방향 전환
        nr = r + dr[d]
        nc = c + dc[d]

    # 위치 업데이트
    r, c = nr, nc

else:
    # 만약 K가 좌석 수를 초과하면 0을 출력
    if K > C * R:
        print(0)