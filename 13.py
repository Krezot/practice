h = int(input("Часы (от 0 до 23): "))
m = int(input("Минуты (от 0 до 59): "))
s = int(input("Секунды (от 0 до 59): "))
if 0 < h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
    h = h % 12
    t_s = h * 3600 + m * 60 + s
    angle = (t_s / 43200) * 360
    print("The angle is ", angle)
else:
    print("Try again")
