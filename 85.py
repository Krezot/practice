N = int(input())
k = list(map(int, input().split()))
possibility = False
for i in range(N):
    temp = k[:i] + k[i + 1 :]
    increase = True
    for j in range(1, len(temp)):
        if temp[j - 1] > temp[j]:
            increase = False
            break
    if increase == True:
        possibility = True
        break
if possibility == True:
    print("да")
else:
    print("нет")
