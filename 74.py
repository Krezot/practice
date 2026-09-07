N = int(input())
z = list(map(int, input().split()))
from collections import Counter

freq = Counter(z)
m_count = max(freq.values())
if m_count <= (N + 1) // 2:
    print("да")
else:
    print("нет")
