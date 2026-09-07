q = list(map(int, input().split()))
e = list(map(int, input().split()))
N = len(q)
f = False
for i in range(N):
    # сдвиг вправо
    s = q[-i] + q[:-i] if i > 0 else q
    if s == e:
        f = True
        break
if f == True:
    print("да")
else:
    print("нет")
