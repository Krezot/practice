N = int(input())
x = list(map(int, input().split()))
seen = set()
l = 0
m_len = 0
for i in range(N):
    while x[i] in seen:
        seen.remove(x[i])
        l += 1
        seen.add(x[i])
        m_len = max(m_len, i - l + 1)
print(m_len)
