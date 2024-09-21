T = int(input())

for _ in range(T):
    bracket = input()
    stack = []
    answer = 'YES'

    for i in bracket:
        if i == '(':
            stack.append(i)

        if i == ')':
            # 비어 있다면 종료
            if not stack:
                answer = 'NO'
                break

            # 괄호 짝을 검사
            left = stack.pop()
            # 짝이 맞지 않는다면 종료
            if not (left == '(' and i == ')'):
                answer = 'NO'
                break

    # 루프가 끝났지만 남아있는 괄호가 존재한다면 answer 0
    if stack:
        answer = 'NO'

    # 결과 출력
    print(answer)