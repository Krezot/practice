h = list(map(int, input().split()))
e = list(map(int, input().split()))
i = 0
j = 0
result = []
while i < len(h) and j < len(e):
    if h[i] < e[j]:
        if not result or result[-1] != h[i]:
            result.append(h[i])
        i += 1
    elif h[i] > e[j]:
        if not result or result[-1] != e[j]:
            result.append(e[j])
        j += 1
    else:
        if not result or result[-1] != h[i]:
            result.append(h[i])
        i += 1
        j += 1
while i < len(h):
    if not result or result[-1] != h[i]:
        result.append(h[i])
    i += 1
while j < len(e):
    if not result or result[-1] != e[j]:
        result.append(e[j])
    j += 1
print(*result)
