N, M, L = map(int, input().split()) 

people = [0] * N  # 각 사람이 공을 받은 횟수를 저장할 리스트
idx = 0  # 첫 번째 사람의 인덱스는 0
people[idx] = 1  # 최초로 첫 번째 사람이 공을 받았다고 설정
cnt = 0  # 공을 던지는 총 횟수

while people[idx] != M:  # 공을 받은 횟수가 M이 될 때까지 반복
    cnt += 1  # 공을 던지는 횟수 증가

    if people[idx] % 2 == 1:  # 홀수 번 공을 받은 경우 -> 시계 방향으로 이동
        idx = (idx + L) % N  # L만큼 이동하고 N을 넘으면 순환하도록 % 연산
    else:  # 짝수 번 공을 받은 경우 -> 반시계 방향으로 이동
        idx = (idx - L) % N  # L만큼 이동하고 N을 넘으면 순환하도록 % 연산

    people[idx] += 1  # 이동한 사람이 공을 받음

print(cnt)  # 총 공을 던진 횟수 출력
