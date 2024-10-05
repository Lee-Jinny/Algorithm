from collections import deque  # deque를 import 해야 합니다.

# 상 하 좌 우
dr = [-1, 1, 0, 0]  # 행 이동
dc = [0, 0, -1, 1]  # 열 이동

# sr, sc = 시작점
def bfs(sr, sc, N):
    visited = [[0] * N for _ in range(N)]
    q = deque()  # deque로 큐를 초기화합니다.
    q.append((sr, sc))
    visited[sr][sc] = 1

    # 탐색 시작
    while q:
        r, c = q.popleft()

        # 종료 조건: 도착
        if maze[r][c] == 3:
            return 1

        # 도착하지 않았다면 다음 탐색
        for d in range(4):
            nr = r + dr[d]  # 방향에 따라 행 업데이트
            nc = c + dc[d]  # 방향에 따라 열 업데이트

            # 유효성 검사
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and maze[nr][nc] != 1:
                q.append((nr, nc))
                visited[nr][nc] = 1  # 방문 표시

    return 0

T = 10
for tc in range(1, T + 1):
    input()  # 테스트 케이스 번호
    N = 16
    maze = [list(map(int, input().strip())) for _ in range(N)]  # 입력 받기, strip()을 통해 불필요한 공백 제거
    answer = bfs(1, 1, N)  # 시작 위치는 (1, 1)로 설정

    print(f'#{tc} {answer}')  # 결과 출력
