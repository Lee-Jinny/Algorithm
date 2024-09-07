T = int(input())

for tc in range(1, T+1):
    memory = input()  # 현재 메모리 상태 입력
    cnt = 0
    current = '0'  # 메모리의 초기 상태

    for i in memory:
        if i != current:  # 현재 비트가 이전와 다르면 변경
            cnt += 1
            current = i  # 현재 상태 업데이트

    print(f'#{tc} {cnt}')