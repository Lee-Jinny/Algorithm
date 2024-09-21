import sys
input = sys.stdin.readline

# 탑의 개수
N = int(input())
# N개의 탑들의 높이
tower = list(map(int, input().split()))
answer = [0] * N # 결과 저장
stack = []


for i in range(N):
    # 스택이 비어 있지 않고, 현재 탑이 스택에 저장된 탑보다 높으면 스택에서 제거
    while stack and tower[stack[-1]] < tower[i]:
        stack.pop()

    # 스택이 비어 있지 않다면, 현재 탑이 신호를 수신할 수 있는 탑이 스택의 꼭대기 탑
    if stack:
        answer[i] = stack[-1] + 1  # 인덱스를 1-based로 변환

    # 현재 탑의 인덱스를 스택에 추가
    stack.append(i)

# 결과 출력
print(*answer)


