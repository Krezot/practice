month = int(input("Введите номер месяца (1-12): "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 день")
elif month in [4, 6, 9, 11]:
    print("30 день")
else:
    print("28 день")
