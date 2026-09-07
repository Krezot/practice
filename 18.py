a = float(input("Сторона треугольника: "))
b = float(input("Сторона треугольника: "))
c = float(input("Сторона треугольника: "))
if a + b > c and a + c > b and b + c > a:
    print("Данный треугольник существует")
else:
    print("Не существует")
