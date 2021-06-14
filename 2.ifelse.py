# *** Логические операции ***

z = 3
w = 2

# операции сравнения

# операция "равно"
#  мы с прашиваем " значиение z равно зачению w?" 
#  ответ будет присвоен переменной result
result = z == w 

# операция "не равно"
result = z != w

# опеарция "меньше"
result = z < w

# операция "больше"
result = z > w

# операция "меньше или равно"
result = z <= w

# операция "больше или равно"
result = z >= w


# чистые логические операции

var_1 = True
var_2 = True

# оператор "НЕ" (NOT, инверсия)
result = not var_1

#  оператор "И" (AND, )
#  возврашает True только тогда, когда обе перменных являються True
result = var_1 and var_2

# оператор "ИЛИ" (OR)
#  возврашает False только тогда, когда обе перменных являються False
result = var_1 and var_2

# print(result)

# *** Условные операторы ***

# Оператор if ("если")
# if False:
#     w = "Hello"
#     print(w)

z = 20 

# if z < 3: # "если"
#     print("Тестовое сообшение Меньше")
# else: # "иначе" 
#     print ("не меньше")

v = "r"

if v == "B":
    res = "Literal B"
elif  v == "A":
    res = "Literal A"
elif  v == "D":
    res = "Literal D"
elif  v == "W":
    res = "Literal W"
else:
    res = "не понятный мне символ))))"

print (res)
