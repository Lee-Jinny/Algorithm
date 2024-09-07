def tycoon(n,m,k, t):
    # 손님 도착 시간 정렬
    t.sort()

    for i in range(n):
        # (t[i] // m) 은 i번째 손님이 도착한 시간까지 붕어빵을 몇번 구웠는지(회수)
        # K(한 번에 만드는 붕어빵 수)를 곱하면 그때까지 만들어진 붕어빵의 총 개수
        making = (t[i]//m)*k

        # 손님 수가 지금까지 만든 붕어빵 수 보다 많이지면 안됨
        if making < i + 1:
            return 'Impossible'

    return 'Possible'






T = int(input())

for tc in range(1, T+1):
    # N명에게 판매, M초에 K개 생산
    N, M, K = map(int, input().split())
    # 사람들이 도착하는 시간
    time = list(map(int, input().split()))

    result = tycoon(N,M,K, time)
    print(f'#{tc} {result}')
