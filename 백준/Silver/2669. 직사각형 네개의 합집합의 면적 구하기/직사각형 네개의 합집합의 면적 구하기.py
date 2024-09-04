square = [[0] * 101 for _ in range(101)]

cnt = 0  # 직사각형이 차지하는 총 면적을 저장할 변수

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())  # 각 직사각형의 좌표 입력

    # 직사각형의 좌표에 해당하는 구역을 1로 표시
    for r in range(x1, x2):
        for c in range(y1, y2):
            # 해당 구역이 아직 직사각형에 포함되지 않았다면
            if square[r][c] == 0:
                square[r][c] = 1  # 해당 구역을 직사각형으로 표시
                cnt += 1  # 면적 카운트 증가


print(cnt)
