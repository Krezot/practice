N = int(input())
e = list(map(int, input().split()))
s = set()
for i in range(N - 2):
    triple = sorted(e[i : i + 3])
    s.add(triple[1])
print(len(s))
