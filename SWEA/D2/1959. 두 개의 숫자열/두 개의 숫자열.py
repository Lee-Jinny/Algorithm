T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 긴 숫자열을 무조건 A에 넣어서 계산하기 편하도록
    if N < M:
        A, B = B, A
        N, M = M, N # 두 문자열의 길이도 교환

    max_sum = -float('inf')
    # 긴 숫자열에서 곱하기 대상의 시작점: 0부터 N-M
    for i in range(N-M+1):
        tmp = 0

        for j in range(M):
            tmp += A[i + j] * B[j]
        # 최댓값을 갱신
        max_sum = max(tmp, max_sum)

    print(f'#{tc} {max_sum}')




