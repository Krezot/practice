n = int(input("Input flat number (from 1 to 20): "))
if 1 <= n <= 20:
    floor = (n - 1) // 4 + 1
    NF = (n - 1) % 4 + 1  # Порядковый номер квартиры на этаже
    print("The flat is on floor", floor, "The flat is", NF, "-th.")
else:
    print("The flat doesn't exist :)")
