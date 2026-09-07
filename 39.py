N = int(input())
for i in range(1, N + 1):
    num: int = 0
    for j in range(1, i + 1):
        num = num * 10 + j
    print(num)
