a = input()

for i in "0123456789":
    if a.count(i) == 1:
        print(i)
        break
else:
    print("нет")
