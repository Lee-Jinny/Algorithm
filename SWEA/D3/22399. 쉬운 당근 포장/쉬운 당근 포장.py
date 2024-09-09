# import sys
# sys.stdin = open('input.txt', 'r')



T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 수확한 당근 개수
    carrot = list(map(int, input().split()))
    carrot.sort()
    min_carrot = float('inf')
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            if carrot[i] == carrot[i - 1] or carrot[j] == carrot[j - 1]:
                continue

            small = carrot[:i]
            midium = carrot[i:j]
            big = carrot[j:]

            s = len(small)
            m = len(midium)
            b = len(big)

            diff = max(abs(s - m), abs(m - b), abs(b - s))
            min_carrot = min(diff, min_carrot)

    if min_carrot == float('inf'):
        min_carrot = -1

    print(f'#{tc} {min_carrot}')