from collections import deque
import sys

input = sys.stdin.readline

# 입력받은 정수 N (명령의 개수)
N = int(input())

# deque 생성
dq = deque([])

# N번의 명령 처리
for _ in range(N):
    order = input().strip().split()

    if order[0] == 'push':  # 명령이 'push'일 때
        dq.append(int(order[1]))  # 뒤에 숫자를 추가

    elif order[0] == 'pop':  # 명령이 'pop'일 때
        if dq:  # deque가 비어있지 않으면
            print(dq.popleft())  # 가장 앞에 있는 값을 빼고 출력
        else:
            print(-1)  # 비어있으면 -1 출력

    elif order[0] == 'size':  # 명령이 'size'일 때
        print(len(dq))  # deque 크기 출력

    elif order[0] == 'empty':  # 명령이 'empty'일 때
        if dq:  # deque가 비어있지 않으면
            print(0)  # 0 출력 (비어있지 않음)
        else:
            print(1)  # 1 출력 (비어있음)

    elif order[0] == 'front':  # 명령이 'front'일 때
        if dq:  # deque가 비어있지 않으면
            print(dq[0])  # 가장 앞에 있는 값 출력
        else:
            print(-1)  # 비어있으면 -1 출력

    elif order[0] == 'back':  # 명령이 'back'일 때
        if dq:  # deque가 비어있지 않으면
            print(dq[-1])  # 가장 뒤에 있는 값 출력
        else:
            print(-1)  # 비어있으면 -1 출력
