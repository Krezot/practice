a = int(input())

for i in range(0, 10):
    t = a
    c = 0
    while t > 0:
        if t % 10 == i:
            c += 1
        t //= 10
    print(i, c)
