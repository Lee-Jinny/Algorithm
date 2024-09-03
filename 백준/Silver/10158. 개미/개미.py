# 입력 받기
w, h = map(int, input().split())  # w x h 격자 공간
p, q = map(int, input().split())  # 초기 좌표
t = int(input())                  # t 시간 후

# x 좌표 계산
x = (p + t) % (2 * w)
if x > w:
    x = 2 * w - x  # 반사된 좌표로 변환

# y 좌표 계산
y = (q + t) % (2 * h)
if y > h:
    y = 2 * h - y  # 반사된 좌표로 변환

# 결과 출력
print(x, y)
