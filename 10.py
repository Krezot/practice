n = int(input("Input flat number (from 1 to 15): "))
if 1 <= n <= 15:
    floor = (n - 1) // 3 + 1
    print("The flat is on floor", floor)
else:
    print("The flat doesn't exist :)")
