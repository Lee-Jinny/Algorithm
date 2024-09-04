# 입력 받기
w, h = map(int, input().split())  # 가로와 세로
N = int(input())  # 잘라야 하는 점선의 개수

width = [0, w]  # 가로의 경계점 (0과 w 포함)
height = [0, h]  # 세로의 경계점 (0과 h 포함)

# 잘라야 하는 점선들의 위치 입력 받기
for _ in range(N):
    direction, num = map(int, input().split())
    if direction == 0:  # 가로로 자를 경우 세로 길이 영향
        height.append(num)
    else:  # 세로로 자를 경우 가로 길이 영향
        width.append(num)

# 정렬
width.sort()
height.sort()

# 가로에서 인접한 점선들 사이의 최대 차이 구하기
max_width = width[0]
for i in range(1, len(width)):
    max_width = max(max_width, width[i] - width[i - 1])

# 세로에서 인접한 점선들 사이의 최대 차이 구하기
max_height = height[0]
for i in range(1, len(height)):
    max_height = max(max_height, height[i] - height[i - 1])

# 가장 큰 직사각형의 넓이 계산
answer = max_width * max_height
print(answer)

