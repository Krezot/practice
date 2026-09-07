N = int(input())
b = list(map(int, input().split()))
t = False
for i in range(1, N - 1):
    if b[i - 1] < b[i] < b[i + 1]:
        t = True
        print(b[i])
        break
    else:
        print("NO")
