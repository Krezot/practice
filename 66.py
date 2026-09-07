N = int(input())
v = list(map(int, input().split()))
pfx = 0
seen = {0: -1}
mx_len = 0
for i, x in enumerate(v):
    pfx += x
    if pfx in seen:
        mx_len = max(mx_len, i - seen[pfx])
    else:
        seen[pfx] = i
print(mx_len)
