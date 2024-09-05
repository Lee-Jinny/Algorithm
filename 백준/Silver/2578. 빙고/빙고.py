def check(game):
    bingo = 0  # bingo를 함수 내부에서 초기화

    # 가로
    for r in range(5):
        row = 0
        for c in range(5):
            if game[r][c] == 1:
                row += 1
        if row == 5:  # 모든 열을 다 돈 후에 bingo 체크
            bingo += 1

    # 세로
    for c in range(5):
        col = 0
        for r in range(5):
            if game[r][c] == 1:
                col += 1
        if col == 5:  # 모든 행을 다 돈 후에 bingo 체크
            bingo += 1

    # 우하행 대각선
    cross_r = 0  # 대각선 변수는 루프 밖에서 초기화
    for i in range(5):
        if game[i][i] == 1:
            cross_r += 1
    if cross_r == 5:
        bingo += 1

    # 좌하향 대각선
    cross_l = 0  # 대각선 변수는 루프 밖에서 초기화
    for i in range(5):
        if game[i][4-i] == 1:
            cross_l += 1
    if cross_l == 5:
        bingo += 1
    
    return bingo


my_lst = [list(map(int, input().split())) for _ in range(5)]
num = [list(map(int, input().split())) for _ in range(5)]
game = [[0] * 5 for _ in range(5)]

cnt = 0

# 부른 숫자가 내 빙고판에 들어있으면 cnt += 1
for i in range(25):
    for j in range(5):
        for k in range(5):
            if num[i // 5][i % 5] == my_lst[j][k]:  # num[i] -> num[i // 5][i % 5]으로 수정
                game[j][k] = 1
                cnt += 1

    # 빙고 확인 조건
    if cnt >= 12:
        if check(game) >= 3:  # gmae -> game으로 수정
            print(cnt)
            break
