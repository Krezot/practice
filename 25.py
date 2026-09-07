year = int(input("Введите год: "))

# Определяем животное (12-летний цикл)
if year % 12 == 0:
    animal = "Обезьяна"
elif year % 12 == 1:
    animal = "Петух"
elif year % 12 == 2:
    animal = "Собака"
elif year % 12 == 3:
    animal = "Свинья"
elif year % 12 == 4:
    animal = "Крыса"
elif year % 12 == 5:
    animal = "Корова"
elif year % 12 == 6:
    animal = "Тигр"
elif year % 12 == 7:
    animal = "Заяц"
elif year % 12 == 8:
    animal = "Дракон"
elif year % 12 == 9:
    animal = "Змея"
elif year % 12 == 10:
    animal = "Лошадь"
else:
    animal = "Овца"

# Определяем цвет (5-летний цикл, каждый цвет на 2 года)
if year % 10 == 0 or year % 10 == 1:
    color = "Белый"  # Металл
elif year % 10 == 2 or year % 10 == 3:
    color = "Черный"  # Вода
elif year % 10 == 4 or year % 10 == 5:
    color = "Зеленый"  # Дерево
elif year % 10 == 6 or year % 10 == 7:
    color = "Красный"  # Огонь
else:
    color = "Желтый"  # Земля

print(f"{animal}, {color}")
