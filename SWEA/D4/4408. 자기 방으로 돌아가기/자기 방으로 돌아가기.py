T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 돌아갈 학생 수
    aisle = [0] * 201 # 복도 구간

    for _ in range(N):
        start, end = map(int, input().split())  # 현재 방번호와 돌아갈 방 번호
        # 방 번호를 복도 구간으로 변환 (1~400 방 -> 1~200 복도 구간)
        start_aisle = (start +1) // 2
        end_asile = (end+1)//2

        # 순차적으로 처리하기 위해 정렬
        if start_aisle> end_asile:
            start_aisle, end_asile = end_asile, start_aisle
        # 복도 구간의 사용량을 증가
        for i in range(start_aisle, end_asile+1):
            aisle[i] += 1

    # 가장 많이 사용된 복도 구간이 이동 시간의 최소값
    print(f'#{tc} {max(aisle)}')

'''
가장 많이 사용된 복도 구간은 그 구간에서 많은 학생들이 겹쳐서 이동을 해야 하므로,
해당 구간을 기준으로 전체 이동 시간을 결정하게 됨. 
그래서 가장 많이 사용된 복도 구간이 이동 시간의 최소값이 됨
'''

