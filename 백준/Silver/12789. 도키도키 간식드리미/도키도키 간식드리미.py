N = int(input())  # 현재 승환이 앞에 서 있는 학생들의 수

# 학생들이 받은 번호
num = list(map(int, input().split()))

# 스택 생성
stack = []

# 찾아야 할 번호
turn = 1

# 학생들 번호를 차례로 스택에 넣기
for student in num:
    stack.append(student)

    # 만약 목표로 하는 번호를 찾으면 스택에서 꺼내고 찾을 번호 += 1
    while stack and stack[-1] == turn:
        stack.pop()
        turn += 1


# 반복문을 다 돌았는 데도 스택에 값이 남아 있으면 sad
if stack:
    print('Sad')
else:
    print('Nice')