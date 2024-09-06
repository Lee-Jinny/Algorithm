N = int(input())

heights = [0]*(1001)

max_position = 0
max_height = 0


for _ in range(N):
    position, height = map(int, input().split())
    heights[position] = height  # 해당 위치에 건물 높이 기록

    # 가장 높은 건물의 위치와 높이 갱신
    if max_height < height:
        max_position, max_height = position, height

# 왼쪽에서 가장 높은 건물까지 면적 계산
area = 0
current_max = 0
for i in range(max_position + 1):
    current_max = max(current_max, heights[i])  # 현재까지의 최대 높이를 갱신
    area += current_max  # 해당 위치의 최대 높이를 면적에 더함

# 오른쪽에서 가장 높은 건물까지 면적 계산
current_max = 0
for i in range(1000, max_position, -1):
    current_max = max(current_max, heights[i])  # 현재까지의 최대 높이를 갱신
    area += current_max  # 해당 위치의 최대 높이를 면적에 더함

print(area)  # 총 면적 출력