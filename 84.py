N = int(input())
q = list(map(int, input().split()))
m_v = max(q)
f_element = q.index(m_v)
l_element = N - 1 - q[::-1].index(m_v)
if f_element == l_element:
    print(0)
else:
    result = len(set(q[f_element + 1 : l_element]))
    print(result)
