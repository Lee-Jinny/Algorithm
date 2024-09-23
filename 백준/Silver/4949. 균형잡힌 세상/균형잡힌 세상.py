while True:
    code = input()
    stack = []
    answer = 'yes'
    if code == '.':
        break
    else:
        for i in code:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)

            elif i == ')' or i == ']' or i == '}':  # else if로 수정
                if not stack:
                    answer = 'no'
                    break

                left = stack.pop()
                if (left == '(' and i != ')') or (left == '[' and i != ']') or (left == '{' and i != '}'):
                    answer = 'no'
                    break
        if stack:  # 모든 문자를 처리했는데도 stack이 비지 않으면 no
            answer = 'no'
        print(answer)
