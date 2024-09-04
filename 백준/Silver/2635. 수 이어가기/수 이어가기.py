N = int(input())

result = [N]  # 초기 수열 저장

# 두 번째 수로 가능한 모든 경우의 수를 시도
for i in range(1, N + 1):
    tmp = [N, i]  # 첫 번째와 두 번째 수 저장
    
    # 수열 생성
    while tmp[-1] >= 0:  # 음수가 되면 종료
        tmp.append(tmp[-2] - tmp[-1])
    
    tmp.pop()  # 마지막 음수를 제거
    
    # 더 긴 수열을 발견하면 갱신
    if len(tmp) > len(result):
        result = tmp

# 결과 출력
print(len(result))
print(*result)
