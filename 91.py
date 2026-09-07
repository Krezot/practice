N = int(input())
t = list(map(int, input().split()))
f = {}
for i in t:
    f[i] = f.get(i, 0) + 1
max_f = max(f.values())
for i in t:
    if f[i] == max_f:
        print(i, max_f)
        break
