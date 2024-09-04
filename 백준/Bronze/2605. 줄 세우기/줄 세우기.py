N = int(input())  # 학생 수
pick_num = list(map(int,input().split()))  # 학생들이 뽑은 번호
line = [n for n in range(1, N+1)]

for i in range(N):
    change, student = pick_num[i], line[i]  # 이동할 칸 수, 학생 번호
    for j in range(i, i-change, -1):
        line[j] = line[j-1]
    line[i - change] = student
print(*line)
