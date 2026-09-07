N = int(input())
k = list(map(int, input().split()))
seen = set()
result = []
for i in k:
    if i not in seen:
        seen.add(i)
        result.append(i)
print(*result)
