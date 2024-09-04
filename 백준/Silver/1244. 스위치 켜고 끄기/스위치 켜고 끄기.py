def onoff(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return

N = int(input())  # 스위치 개수

# 각 스위치의 상태, 1부터 시작해야 하므로 앞에 -1 추가
switch = [-1] + list(map(int, input().split()))  
student = int(input())  # 학생 수

for _ in range(student):
    sex, num = map(int, input().split())
    
    # 남학생의 경우
    if sex == 1:
        for i in range(num, N+1, num):
            onoff(i)
    
    # 여학생의 경우
    elif sex == 2:
        onoff(num)
        for k in range(1, N//2 + 1):  # k는 1부터 시작 (자기 자신을 제외한 대칭 비교)
            if num + k > N or num - k <= 0:
                break
            if switch[num + k] == switch[num - k]:
                onoff(num + k)
                onoff(num - k)
            else:
                break

# 스위치 상태 출력
for j in range(1, N+1):
    print(switch[j], end=" ")
    if j % 20 == 0:  # 한 줄에 20개씩 출력
        print()
