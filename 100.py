from Task97 import possible

N = int(input())
a = list(map(int, input().split()))
stability = True
for i in range(1, N - 1):
    if a[i] < min(a[i - 1], a[i + 1]) or a[i] > max(a[i - 1], a[i + 1]):
        stability = False
        break
if stability:
    print("ДА")
else:
    possible = False
    for j in range(N):
        temp = a[::j] + a[j + 1 :]
        result = True
        for i in range(1, len(temp) - 1):
            if temp[i] < min(temp[i - 1], temp[i + 1]) or temp[i] > max(
                temp[i - 1], temp[i + 1]
            ):
                result = False
                break
        if result == True:
            possible = True
            break
    if possible:
        print("да")
    else:
        print("нет")
