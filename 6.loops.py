# *** Циклы ***

# Оператор цикла While - Переводиться как "Пока" - Бесконечный цикл

# Прерывается сочетанием клавишь Ctrl+C
# while True:
#     print("Hello")

# g = 10
# while g >= 0:
#     g = g - 1
#     g -= 1
#     print(f"Hello {g}")

# Инструкция прерывания цикла по дополнительному условию
# g = 10
# while g > 0:
#     print(f"Hello {g}")
#     if g == 5:
#         # Прерывает цикл
#         break
#     g -= 1


# --- Оператор цикла for ---
# 1. читает значение из интерирумых объектов по порядку (слева на право)
# 2. значение присваивает в свою переменную (хранит временно)
# 3. вполняет блок кода своего тела

my_list = [10,20,30,40,50]

# for i in my_list:
#     print(i)

# for i in my_list[::-1]:
#     print(i)


# генератор списка 

# создание списка чисел в диапазоне от 10 до 100 с шагом 10
num_list = [num * 2 for num in range(10, 100,10)]

print(num_list)