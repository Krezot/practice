N = int(input())
q = list(map(int, input().split()))
if N == 0:
    print(0)
else:
    max_len = 1
    c = 1
    for i in range(1, N):
        if abs(q[i] - q[i - 1]) == 1:
            c += 1
            max_len = max(max_len, c)
        else:
            c = 1
    print(max_len)
