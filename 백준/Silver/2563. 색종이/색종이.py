N = int(input())

colored_paper = [[0] * 100 for _ in range(100)]  # 100 * 100 크기

for _ in range(N):
    y1, x1 = map(int, input().split())

    for r in range(x1, x1 + 10):
        for c in range(y1, y1 + 10):
            colored_paper[r][c] = 1  # 색종이가 덮이는 부분을 1로 설정

result = 0
for r in range(100):
    for c in range(100):
        if colored_paper[r][c] == 1:  # 색종이가 덮인 부분이면
            result += 1  # 면적에 추가

print(result)
