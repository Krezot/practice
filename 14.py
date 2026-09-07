y = float(input("input angle of the clock hand (from 0 to 360): "))
if y < 360:
    min_passed = int((y / 360) * 720)
    hours_passed = int((min_passed // 60))
    print("The hours passed is", hours_passed)
    print("The minutes passed is", min_passed)
else:
    print("Try again")
