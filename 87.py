N = int(input())
f = list(map(int, input().split()))
sorted_f = sorted(f)
diff = []
for i in range(N):
    if f[i] != sorted_f[i]:
        diff.append(i)
if len(diff) == 0:
    print("ДА")
elif len(diff) == 2:
    i, j = diff[0], diff[1]
    f[i], f[j] = f[j], f[i]
    result = True
    for k in range(1, N):
        if f[k] <= f[k - 1]:
            result = False
            break
    if result == True:
        print("да")
    else:
        print("нет")
else:
    print("нет")
