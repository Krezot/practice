a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))

c = b**0.5
if c < a:
    b = b * 5
    print(a, b)
