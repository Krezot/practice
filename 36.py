N = int(input())
t = True
if N < 2:
    t = False
else:
    i = 2
    while i * i <= N:
        if N % i == 0:
            t = False
            break
        i += 1
if t == True:
    print("Да")
else:
    print("Нет")
