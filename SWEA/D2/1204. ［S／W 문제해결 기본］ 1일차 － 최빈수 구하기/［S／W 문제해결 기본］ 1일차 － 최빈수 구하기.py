T = int(input())  # 테스트 케이스 수 입력

for _ in range(1, T+1):
    tc = int(input())  # 테스트 케이스 번호 입력
    num = [0] * 101  # 점수는 0부터 100까지이므로 101개의 리스트 생성
    score = list(map(int, input().split()))  # 점수 리스트 입력

    # 각 점수의 빈도를 카운트
    for i in score:
        num[i] += 1  # 해당 점수의 빈도를 증가

    # 최빈값 찾기 (빈도가 가장 높은 점수를 찾아야 함)
    max_frequency = max(num)  # 가장 높은 빈도를 찾음
    mode = 0  # 최빈값을 저장할 변수

    # 빈도가 같은 경우 더 높은 점수를 선택해야 함
    for i in range(100, -1, -1):  # 점수는 0부터 100까지, 높은 점수부터 확인
        if num[i] == max_frequency:  # 현재 점수가 최빈값인지 확인
            mode = i
            break  # 가장 높은 점수부터 확인하므로 첫 번째로 발견된 최빈값이 가장 높은 점수임

    # 결과 출력
    print(f'#{tc} {mode}')
