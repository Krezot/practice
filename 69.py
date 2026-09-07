N = int(input())
r = list(map(int, input().split()))
m_sum = r[0]
c_sum = r[0]
start = 0
end = 0
temp = 0
for i in range(1, N):
    if c_sum < 0:
        c_sum = r[i]
        temp = i
    else:
        c_sum += r[i]
    if c_sum > m_sum:
        m_sum = c_sum
        start = temp
        end = i
print(start, end)
