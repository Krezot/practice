a = list(map(int, input().split()))
u = list(map(int, input().split()))
i = 0
j = 0
result = []
while i < len(a) and j < len(u):
    if a[i] == u[i]:
        result.append(a[i])
        i += 1
        j += 1
    elif a[i] < u[i]:
        i += 1
    else:
        j += 1
print(*result)
