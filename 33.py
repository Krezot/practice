a = int(input())
n = 0
c = 10
while a != 0:
    n = n + (a % 10)
    n = n * c
    a = a // 10
n = n // 10
print(n)
