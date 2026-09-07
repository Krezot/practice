N = map(int, input().split())
M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i = j = 0
merge = []
while i < N and j < M:
    if a[i] < b[j]:
        merge.append(a[i])
        i += 1
    else:
        merge.append(b[j])
        j += 1
merge.extend(a[i:])
merge.extend(b[j:])
print(*merge)
