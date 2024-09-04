height = [int(input()) for _ in range(9)]
height.sort()

def find_dwarfs():
    for i in range(9):
        for j in range(i+1, 9):
            if sum(height) - (height[i] + height[j]) == 100:
                for k in range(9):
                    if i == k or j == k:
                        continue
                    print(height[k])
                return

find_dwarfs()
