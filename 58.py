N = int(input())
b = list(map(int, input().split()))
t = False
for i in range(N - 2, 0, -1):
    if b[i - 1] < b[i] < b[i + 1]:
        print(i)
        t = True
        break
    else:
        print("NO")
