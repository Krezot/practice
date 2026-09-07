N = int(input())
v = list(map(int, input().split()))
m_len = 0
c = 0
for i in v:
    if i % 2 == 0:
        c += 1
        m_len = max(m_len, c)
    else:
        c = 0
print(m_len)
