K = int(input())

stack = []
sum_n = 0

for _ in range(K):
    num = int(input())

    if num == 0:
        stack.pop()
    else:
        stack.append(num)

for i in stack:
    sum_n += i

print(sum_n)