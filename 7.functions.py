# *** Функции ***

# Встроенная функция ввода данных 
# data = input("Введите данные: ")

# print(f"Вы вели вот это - {data}")

# Создание (определние) функции

# 1 варимант. Функция, принимающая данные (обладающая агументами)
def func_1(arg_1):
    s = arg_1 ** 2
    w = s + 10
    print(f"Результат: {w}")

#  Вызов функции
# func_1(1000)

def func_2(a, b, c):
    res = a + b + c
    res += 200 
    print(res)

# func_2(10, 5, 2)

def func_3(arg_1, arg_2=100):
    print(arg_1 * arg_2)

# func_3(20, 10)
# func_3(100)
# func_3(3.14)


# 2 вариант. Функция, возвращающая данные
def func_4(arg_1, arg_2):
    res = arg_1 + arg_2
    return res

# d = func_4(10, 10)    

def func_5(x, y):
    res_1 = x * y
    res_2 = x / y
    return res_1, res_2, x

# первый способ приёма (отлова) данных
d_1 = func_5 (10, 2)
# второй способ приёма данных
a, b, c = func_5 (10, 2)

# print(d_1)
# print(d_1[0])

# print(a, b, c)
# print(b)


# *** Безымянные функции (лямбда-выражения, лямбда-функции) ***

# Особенности: 
# - Всегда обладает аргументами 
# - Всегда возвращает результат

# Привер 1. Лямбда внутри генератора списка
my_list = [(lambda arg_1: arg_1.upper())(i) for i in "hello"]

# Привер 2. Словарь Лямбда-выражений 
my_lambdas = {
    "*": lambda arg_1, arg_2: arg_1 * arg_2, 
    "+": lambda W, Z: W + Z
}

# print(my_lambdas["+"](5, 2))
# print(my_lambdas["*"](5, 3))


# *** декоратор ***

# Декоратор - функция, обертывающая другую (таргетную) функцию

# Декоратор
def my_decorator(func_object):
    # функция-обертка
    def wrapper(w):
        # доп функциональность ДО вызова целевой функции
        print("Before")
        w = w + 2
        # вызов целевой функции
        func_object(w)
        # доп функциональность ПОСЛЕ вызова целевой функции 
        print("After")
    # возврат объекта функции-обёртки 
    return wrapper

# новый способ примерения дикоратора
@my_decorator
# целефа (таргетная) функция
def target_func(arg_1):
    print("Hello! I am target func :)", arg_1)

#  старый способ применения декоратора
# target_func = my_decorator(target_func)

target_func(10)

