N = int(input())  # 색종이의 개수 입력

# 101 x 101 크기의 격자 생성 (모두 0으로 초기화)
colored_paper = [[0] * 101 for _ in range(101)]

# 색종이 위치 입력 및 격자에 색종이 영역 표시
for _ in range(N):
    y1, x1 = map(int, input().split())
    for r in range(x1, x1 + 10):
        for c in range(y1, y1 + 10):
            colored_paper[r][c] = 1  # 색종이가 덮이는 부분을 1로 설정

# 둘레 계산을 위한 변수
ans = 0

for i in range(101):
    for j in range(101):
        if colored_paper[i][j] == 1:
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if colored_paper[i+x][j+y] == 0:
                    ans+=1

print(ans)
