a = int(input())
mdigit = 0
while a > 0:
    d = a % 10
    if d > mdigit:
        mdigit = d
    a = a // 10
print(mdigit)
