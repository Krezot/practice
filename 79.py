N = int(input())
q = list(map(int, input().split()))
pref = 0
f = False
for i in q:
    if i == pref:
        f = True
        break
    else:
        pref += i
if f == True:
    print("да")
else:
    print("нет")
