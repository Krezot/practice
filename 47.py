N = int(input())

for i in range(2, N + 1):
    s = True
    j = 2
    while j * j <= i:
        if i % j == 0:
            s = False
            break
        j += 1
    if s:
        print(i, end=" ")
