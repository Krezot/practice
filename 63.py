N = int(input())
c = list(map(int, input().split()))
freq = {}
for i in c:
    freq[i] = freq.get(i, 0) + 1
max_freq = max(freq.values())
for i in c:
    if freq[i] == max_freq:
        print(i)
        break
