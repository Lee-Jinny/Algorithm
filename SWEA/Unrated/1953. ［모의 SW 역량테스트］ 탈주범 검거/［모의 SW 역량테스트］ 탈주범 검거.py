from collections import deque

#     상, 우, 하, 좌  좌표이동
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 터널 타입 설정
tunnel_type = {
    1: [0, 1, 2, 3],  # 상, 우, 하, 좌
    2: [0, 2],  # 상, 하
    3: [1, 3],  # 좌, 우
    4: [0, 1],  # 상, 우
    5: [1, 2],  # 하, 우
    6: [2, 3],  # 하, 좌
    7: [0, 3]   # 상, 좌
}

# 연결되어 있는지 확인
reverse_dir = [2, 3, 0, 1]  # 상 우 하 좌의 각각 반대 방향 인덱스



# BFS 탐색 함수
def bfs(R, C, N, M, L, tunnel):
    # 방문 배열 (N x M) 초기화
    visited = [[0] * M for _ in range(N)]
    dq = deque([(R, C, 1)])  # 시작 위치 (R, C)와 시간 1로 시작
    visited[R][C] = 1  # 시작점 방문 처리
    count = 1  # 첫 시작점도 위치 가능하므로 1로 시작

    while dq:
        r, c, time = dq.popleft()

        # 종료 조건: 경과 시간이 L에 도달
        if time == L:
            continue

        current_type= tunnel[r][c]

        # 현재 터널에서 이동 가능한 방향으로 탐색
        for d in tunnel_type[current_type]:
            nr = r + dr[d]
            nc = c + dc[d]

            # 유효한 범위 내에서만 탐색
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                next_type = tunnel[nr][nc]

                # 다음 위치에 터널이 있고, 이동 가능한 방향이면
                if next_type != 0 and reverse_dir[d] in tunnel_type[next_type]:
                    visited[nr][nc] = 1
                    dq.append((nr, nc, time + 1))
                    count += 1

    return count



T = int(input())  # 테스트 케이스 수
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())  # N: 세로, M: 가로, R, C: 맨홀 위치, L: 경과 시간
    tunnel = [list(map(int, input().split())) for _ in range(N)]  # 지하 터널 지도 입력

    # BFS를 통해 탈주범이 있을 수 있는 장소의 개수 구하기
    result = bfs(R, C, N, M, L, tunnel)

    # 결과 출력
    print(f'#{tc} {result}')


