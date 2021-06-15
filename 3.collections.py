# *** Коллекции (контейнеры, структыры данных) ***

# ** Список (list) **

# Создание пустого списка 
my_list = []
my_list = list() # второй мариант

# документ рекомендательного характера (PEP8) стилистка когда.

# Добавление объекта (элемента) в список 
my_list.append(100)                        # первый элемент / счёт начинаеться с нуля(0)
my_list.append(3.14) # вешественое число. Число с палавюшей точкой
my_list.append("Hello") # строка.
my_list.append([10,20,30])                 # 4й элемент

# print(my_list)

# Чтоение значений элемента 
# прямая индексация 
# в квадратую скобку указываем инжекс необходимого элемента
el = my_list[2]
el = my_list[3][1]  # вызов скисков псоледовательно 

# обратная индексация
el = my_list[-1] # последний элемент . наичаеться не с нуля (0)

# замена значения элемента
my_list[0] = 2000

#  удаление элемента по значению
# my_list.remove(3.14)

# Удаление элемента по индексу 
del my_list[-1]

# Срез списка
s = "Hello, world"
my_list = list(s)

my_slice = my_list[2:] #синтаксис среза
my_slice = my_list[2:5] # со второго до пятого 


print(my_list)
print(my_slice)