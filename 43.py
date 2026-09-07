a = int(input())
m1 = m2 = -1
while a > 0:
    d = a % 10
    if d > m1:
        m2 = m1
        m1 = d
    elif d < m2:
        m2 = d
    a = a // 10
if m2 == -1:
    print("нет")
else:
    print(m2)
