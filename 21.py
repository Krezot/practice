a = float(input("Введите число: "))
b = float(input("Введите число: "))
c = float(input("Введите число: "))

min1 = min(a, b, c)

if min1 == a:
    min2 = min(b, c)
elif min1 == b:
    min2 = min(c, b)
elif min1 == c:
    min2 = min(a, b)
print(min1 * min2)
