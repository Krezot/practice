n = int(input())
a = list(map(int, input().split()))
max_len = 1
cur = 1
for i in range(1, n):
    if a[i] < a[i - 1]:
        cur += 1
    else:
        max_len = max(max_len, cur)
        cur = 1
max_len = max(max_len, cur)
print(max_len)
