from collections import deque

# 16진수 -> 10진수 변환 함수
def hex_to_dec(hexa):
    return int(hexa, 16)



# 보물 상자 비밀 번호 찾는 함수
def find(N, K, hexadecimal):
    password = set() # 중복을 제거하기 위함

    # 회전 큐 생성
    dq = deque(hexadecimal)

    # rotate & 한변당 숫자 수 = N//4
    r = N//4
    for i in range(r):
        for j in range(0, N, r):
            num = ''.join(list(dq)[j:j + r])
            password.add(num)

        # 시계 방향 회전 -> dq.rotate(1)
        last = dq.pop()
        dq.appendleft(last)


    # 16 진수 10 진수 로 변환
    decimal = []
    for p in password:
        dec_num = hex_to_dec(p)
        decimal.append(dec_num)

    # 내림 차순 정렬
    sorted_password = sorted(decimal, reverse = True)

    # K 번째로 큰 수 반환
    return sorted_password[K-1]






T = int(input())

for tc in range(1, T+1):
    # N: 숫자의 개수, K: K번째 큰 수
    N, K = map(int, input().split())
    hexadecimal = input()
    result = find(N, K, hexadecimal)
    # 함수 호출
    print(f'#{tc} {result}')


