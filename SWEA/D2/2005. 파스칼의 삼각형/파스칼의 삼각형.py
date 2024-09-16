T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 파스칼 삼각형의 크기 N 입력
    result = []  # 파스칼 삼각형을 저장할 리스트

    # N줄의 파스칼 삼각형 생성
    for i in range(N):
        P = []  # 각 줄의 값을 저장할 리스트
        for j in range(i + 1):  # 각 줄의 요소 계산
            if j == 0 or j == i:  # 첫 번째와 마지막 요소는 항상 1
                P.append(1)
            else:
                # 그 외의 요소는 바로 위 줄의 두 숫자의 합
                P.append(result[i - 1][j] + result[i - 1][j - 1])

        # 현재 줄 P를 결과 리스트에 추가
        result.append(P)

    # 테스트 케이스 번호 출력
    print(f'#{tc}')

    # 파스칼 삼각형 출력
    for i in result:
        # 각 줄의 숫자를 문자열로 변환 후, 공백 없이 출력
        print(' '.join(map(str, i)))
