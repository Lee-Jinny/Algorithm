T = int(input())

for tc in range(1, T+1):
    N = int(input())  # N일
    price = list(map(int, input().split())) # 매매가
    revenue = 0  # 총 수익을 저장할 변수

    max_price = price[-1]  # 초기 최댓값, 뒤에서 부터 확인할 것이므로 인덱스 -1
    for i in range(N-1, -1, -1):
        if price[i] > max_price:
            max_price = price[i]
        revenue += max_price - price[i] # 현재 최댓값과 현재 가격의 차이만큼 더하기

    print(f'#{tc} {revenue}')