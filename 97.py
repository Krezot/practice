N = int(input())
o = list(map(int, input().split()))
m_val = max(o)
possible = set()
for i in range(N):
    temp = o[:i] + o[i + 1 :]
    if temp:
        possible.add(max(temp))
print(*sorted(possible))
