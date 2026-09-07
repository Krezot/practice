a = float(input("Ребро кирпича: "))
b = float(input("Ребро кирпича: "))
c = float(input("Ребро кирпича: "))
x = float(input("Сторона отверстия: "))
y = float(input("Сторона отверстия: "))
if a <= x and b <= y or a <= y and b <= x:
    print("Просунуть сие кирпич реально")
elif a <= x and c <= y or a <= y and c <= x:
    print("Просунуть сие кирпич реально")
elif b <= x and c <= y or b <= y and c <= x:
    print("Просунуть сие кирпич реально")
else:
    print("Просунуть сие кирпич нереально")
