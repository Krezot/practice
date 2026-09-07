N = int(input())
w = list(map(int, input().split()))
m_sum = w[0]
c_sum = w[0]
for i in w[1:]:
    c_sum = max(i, c_sum + i)
    m_sum = max(m_sum, c_sum)
print(m_sum)
