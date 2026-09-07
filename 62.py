N = int(input())
m = list(map(int, input().split()))
count = {}
for i in m:
    count[i] = count.get(i, 0) + 1
result = [i for i in m if count[i] == 1]
if result:
    print(*result)
else:
    print("no")
