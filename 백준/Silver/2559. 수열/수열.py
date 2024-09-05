N, K = map(int, input().split())
temperature = list(map(int, input().split()))

# 첫 번째 윈도우의 합 계산
max_temp = sum(temperature[:K])
current_sum = max_temp

# 슬라이딩 윈도우 기법으로 나머지 구간 탐색
for i in range(1, N - K + 1):
    # 윈도우를 한 칸 오른쪽으로 이동
    current_sum = current_sum - temperature[i - 1] + temperature[i + K - 1]
    if current_sum > max_temp:
        max_temp = current_sum

print(max_temp)
