N = int(input())
q = list(map(int, input().split()))
dis = len(set(q))
if dis == 0:
    print(0)
else:
    from collections import defaultdict

    count = defaultdict(int)
    l = 0
    unique = 0
    min_len = N + 1
    for j in range(N):
        count[q[j]] += 1
        if count[q[j]] == 1:
            unique += 1
        while unique == dis:
            min_len = min(min_len, j - l + 1)
            count[q[j]] -= 1
        if count == 0:
            unique -= 1
        l += 1
    print(min_len)
