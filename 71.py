N = int(input())
o = list(map(int, input().split()))
total = sum(o)
left = 0
count = 0
for i in range(1, N - 1):
    left += o[i]
    if left * 2 == total:
        count += 1
print(count)
