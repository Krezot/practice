N = int(input())
k = list(map(int, input().split()))
count = 0
for i in range(N - 1):
    if (k[i] + k[i + 1]) % 2 == 0:
        count += 1
print(count)
