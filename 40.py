N = int(input())
for i in range(N, 0, -1):
    num = 0
    for j in range(1, i + 1):
        num = num * 10 + j
    print(num)
