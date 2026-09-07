N = int(input())
g = list(map(int, input().split()))
total = sum(g)
if total % 3 != 0:
    print("нет")
else:
    part = total // 3
    c = 0
    count = 0
    for i in range(g):
        c += i
        if c == part:
            count += 1
            c = 0
    if count >= 3:
        print("да")
    else:
        print("нет")
