t = list(map(int, input().split()))
h = list(map(int, input().split()))
n = len(t)
for i in range(n):
    s = t[-i] + t[:-i] if i > 0 else t
    if s == h:
        print(i)
        break
    else:
        print(-1)
