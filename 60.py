n = int(input())
a = list(map(int, input().split()))
print("Да" if a == a[::-1] else "Нет")
