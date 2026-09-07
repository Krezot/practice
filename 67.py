N = int(input())
s = list(map(int, input().split()))
pfx = 0
seen = {0: -1}
f = False
for i, x in enumerate(s):
    pfx += x
    if pfx in seen:
        if i - seen[pfx] >= 2:
            f = True
            break
    else:
        seen[pfx] = i
if f == True:
    print("да")
else:
    print("нет")
