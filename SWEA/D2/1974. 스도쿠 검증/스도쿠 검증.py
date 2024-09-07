def sudoku(arr):
    # 행 탐색
    # arr 행을 한줄씩 확인하면서 1~9가 들어있는지 확인
    for c in range(9):
        for check in range(1, 10):
            if check not in arr[c]:
                return 0

    # 열 탐색
    # 열을 한개씩 tmp 리스트에 담아 숫자가 들어있는지 확인
    for c in range(9):
        tmp = []
        for r in range(9):
            tmp.append(arr[r][c])
        for check in range(1, 10):
            if check not in tmp:
                return 0

    # 9개 정사각형 모양 확인
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            tmp = []
            for i in range(r, r+3):
                for j in range(c, c+ 3):
                    tmp.append(arr[i][j])

            for check in range(1, 10):
                if check not in tmp:
                    return 0

    # 함수 전부 확인했는데 중단이 안되었으면 스도쿠
    return 1






T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    
    result = sudoku(arr)
    print(f'#{tc} {result}')