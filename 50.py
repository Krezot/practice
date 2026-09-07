for n in range(10, 100):
    t = n // 10  # первая цифра (десятки)
    o = n % 10  # вторая цифра (единицы)
    sd = t + o
    if sd * sd == n:
        print(n)
