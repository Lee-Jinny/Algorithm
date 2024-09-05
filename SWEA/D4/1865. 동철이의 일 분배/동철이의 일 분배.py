def divide_work(r, tmp):
    global max_prob
    # 가지치기
    if tmp <= max_prob:
        return

    # 기저 조건
    if r == N:  # 모든 사람의 확률을 곱한 경우
        max_prob = max(tmp, max_prob)
        return

    # 재귀 함수 호출
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            # 확률을 소수로 변환하여 곱함
            divide_work(r + 1, tmp * (prob[r][i]*0.01))
            visited[i] = 0




T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # N명의 직원, 해야 할 일 N개
    prob = [list(map(int, input().split())) for _ in range(N)]
    max_prob = 0  # 최대 확률을 0으로 초기화
    visited = [0] * N

    divide_work(0, 1)
    print(f'#{tc} {max_prob*100:.6f}')
