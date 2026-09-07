N = int(input())
w = list(map(int, input().split()))
res = []
for i in range(N):
    d = 0
    for j in range(i + 1, N):
        if w[i] > w[j]:
            d = j - i
            break
        res.append(d)
print(*res)
