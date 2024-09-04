k = int(input())  # 1m^2의 넓이에 자라는 참외의 개수

directions = []
lengths = []

for _ in range(6):
    direction, length = map(int, input().split())
    directions.append(direction)
    lengths.append(length)

# 큰 직사각형의 가로와 세로 찾기
max_width = 0
max_widx= 0
max_height = 0
max_hidx=0

for i in range(6):
    if directions[i] == 1 or directions[i] == 2:  # 동쪽 또는 서쪽
        if lengths[i] > max_width:
            max_width = lengths[i]
            max_widx = i
    elif directions[i] == 3 or directions[i] == 4:  # 남쪽 또는 북쪽
        if lengths[i] > max_height:
            max_height = lengths[i]
            max_hidx = i



# 작은 직사각형의 가로와 세로 계산
small_width = abs(lengths[max_hidx-1] - lengths[(max_hidx+1) % 6])
small_height = abs(lengths[max_widx-1] - lengths[(max_widx+1) % 6])

# 참외밭의 면적 계산 (큰 직사각형 넓이 - 작은 직사각형 넓이)
bigbox = max_width * max_height
smallbox = small_width * small_height
area = bigbox - smallbox

# 참외의 개수 계산
total_melons = area * k
print(total_melons)
