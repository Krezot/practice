a = int(input())
Oa = a
Ra = 0
while a > 0:
    Ra = Ra * 10 + a % 10
    a //= 10
if Oa == Ra:
    print("Да, одинаково")
else:
    print("Нет, не одинаково")
