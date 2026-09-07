N = int(input())
d = list(map(int, input().split()))
freq = {}
for i in d:
    freq[i] = freq.get(i, 0) + 1
result = []
seen = set()
for i in d:
    if freq[i] == 1 and i not in seen:
        result.append(i)
        seen.add(i)
for i in d:
    if freq[i] > 1 and i not in seen:
        result.append(i)
        seen.add(i)
print(*result)
