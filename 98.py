N = int(input())
y = list(map(int, input().split()))
found = False
for i in range(N):
    seen = set()
    for j in range(i + 1, N):
        if y[j] == y[i]:
            if j - i >= 2:
                found = True
            break
        if y[j] in seen:
            break
        seen.add(y[j])
    if found:
        break
if found:
    print("да")
else:
    print("нет")
