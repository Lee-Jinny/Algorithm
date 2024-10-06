def drive(n, field, commands):
    # RC카 초기 방향과 위치 설정
    r, c = 0, 0
    for i in range(n):
        for j in range(n):
            if field[i][j] == 'X':
                r, c = i, j  # RC카의 초기 위치
                break

    # 방향: 위쪽(0), 오른쪽(1), 아래쪽(2), 왼쪽(3)
    dr = [-1, 0, 1, 0]  # 각 방향에서 이동하는 행 변화량
    dc = [0, 1, 0, -1]  # 각 방향에서 이동하는 열 변화량
    d = 0  # RC카는 처음에 위쪽(0)을 바라봄

    # 명령어 실행
    for cmd in commands:
        if cmd == 'A':
            nr = r + dr[d]  # 현재 방향으로 행 이동
            nc = c + dc[d]  # 현재 방향으로 열 이동
            if 0 <= nr < n and 0 <= nc < n and field[nr][nc] != 'T':  # 나무가 없으면 이동
                r, c = nr, nc
        elif cmd == 'L':
            d = (d + 3) % 4  # 왼쪽으로 90도 회전
        elif cmd == 'R':
            d = (d + 1) % 4  # 오른쪽으로 90도 회전

    return (r, c)


T = int(input())  # 테스트케이스 개수 입력

for tc in range(1, T + 1):
    # 필드의 크기 입력
    N = int(input())
    field = [list(input()) for _ in range(N)]
    
    # 목표 위치 찾기
    target = None
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'Y':
                target = (i, j)
                break

    # 조종을 한 횟수 입력
    Q = int(input())

    # 각 테스트 케이스에 대한 결과 저장
    result = []
    for _ in range(Q):
        # 커맨드 길이, 커맨드
        C, command = input().split()
        
        # RC카 이동 후 위치 확인
        final_pos = drive(N, field, command)
        
        # 최종 위치가 목표 위치와 일치하면 1, 아니면 0
        if final_pos == target:
            result.append(1)
        else:
            result.append(0)

    # 결과 출력
    print(f'#{tc}', *result)
