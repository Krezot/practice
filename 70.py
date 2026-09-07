N = int(input())
u = list(map(int, input().split()))
total = sum(u)
left = 0
p = False
for i in range(1, N - 1):
    left += u[i]
    if left * 2 == total:
        p = True
        break
if p == True:
    print("да")
else:
    print("нет")
