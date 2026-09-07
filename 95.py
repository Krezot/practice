v = list(map(int, input().split()))
u = list(map(int, input().split()))
i = 0
j = 0
result = []
while i < len(v):
    if j < len(u) and v[i] == u[j]:
        i += 1
        j += 1
    elif j < len(u) and v[i] > u[j]:
        j = i + 1
    else:
        result.append(v[i])
        i += 1
print(*result)
