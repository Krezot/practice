N = int(input())
N1 = list(map(int, input().split()))
max_len = 1
cur = 1
for i in range(1, N):
    if N1[i] == N1[i - 1]:
        cur += 1
    else:
        max_len = max(max_len, cur)
        cur = 1
max_len = max(max_len, cur)
print(max_len)
