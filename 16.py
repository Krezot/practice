x1 = float(input("x первого прямоугольника: "))
y1 = float(input("y первого прямоугольника: "))
w1 = float(input("ширина первого: "))
h1 = float(input("высота первого: "))

x2 = float(input("x второго прямоугольника: "))
y2 = float(input("y второго прямоугольника: "))
w2 = float(input("ширина второго: "))
h2 = float(input("высота второго: "))

x1r = x1 + w1  # Верхний правый угол первого прямоугольника
y1t = y1 + h1  # Верхний правый угол первого прямоугольника
x2r = x2 + w2  # Аналогично для второго
y2t = y2 + h2

if x1r > x2r and y1t > y2t and x1r < x2r and y1t < y2t:
    print("все точки первого прямоугольника принадлежат второму")
elif (
    x1r >= x2r
    and y1t >= y2t
    and x1r <= x2r
    and y1t <= y2t
    or x2r >= x1r
    and y2t >= y1t
    and x2r <= x1r
    and y2t <= y1t
):
    print("все точки одного из прямоугольников принадлежат другому")
elif max(x1, x2) < min(x1r, x2r) and max(y1, y2) < max(y1t, y2t):
    print("прямоугольники пересекаются")
else:
    print("Care to try again?")
