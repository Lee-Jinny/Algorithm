from collections import deque
import sys

input = sys.stdin.readline

# N을 입력받고 1부터 N까지의 숫자를 deque에 저장
N = int(input())
dq = deque([i for i in range(1, N+1)])

# 카드가 하나 남을 때까지 반복
while len(dq) > 1:
    dq.popleft()  # 가장 위에 있는 카드를 버림
    change_card = dq.popleft()  # 다음 카드를 뽑아
    dq.append(change_card)  # 그 카드를 맨 뒤로 옮김

# 마지막으로 남은 카드 출력
print(dq[0])
