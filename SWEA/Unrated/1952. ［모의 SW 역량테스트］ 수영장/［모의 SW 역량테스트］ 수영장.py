#import sys
#sys.stdin = open('input.txt', 'r')

# 시작점: 1월 / 누적 금액 0원
# 끝점: 12월

def dfs(month, sum_cost):
    global ans
    # 기저조건: 12월 까지 모두 보았는가?
    if month > 12:
        ans = min(ans, sum_cost)
        return

    # 1일권 구매한 경우 (다음 재귀: 다음달을 확인)
    dfs(month + 1, sum_cost + (days[month] * cost[0]))

    # 1달권 구매한 경우 (다음 재귀:  다음달을 확인)
    dfs(month + 1, sum_cost + cost[1])

    # 3달권 구매한 경우 (다음 재귀:3달 후를 확인)
    dfs(month + 3, sum_cost + cost[2])

    # 1년권 구매한 경우 (다음 재귀: 12달 후를 확인)
    # - [참고] 사실 재귀에서 빼고, 1월에 구입한 비용이랑 비교해도 된다/
    dfs(month + 12, sum_cost + cost[3])






T = int(input())

for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    # 인덱스 헷갈려! 나는 1 ~12 를 쓸거야. 맨 앞에 추가
    days = [0] + list(map(int, input().split()))
    ans = 1e9
    dfs(1, 0)
    print(f'#{tc} {ans}')
