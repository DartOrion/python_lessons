#  *** Генератор паролей ***

import hashlib 
from tkinter import Tk, Label, Entry, Button, StringVar
from typing import Text

def hashing():
    """
    Функция хеширования 

    :Принимает строку паролей и "соль"
    :Возвращает хеш-строку
    """
    # прийм строка чиловекачитаемой пароли с "солью"
    pwd_str = pwd.get()

    # кодирвоания в байт-строку
    byte_str = pwd_str.encode()

    # хеширвоание (применение хеш-функции из модуля hashlib)
    hash_str = hashlib.sha256(byte_str)

    # преобразование хеш-строки специального типа в обычную строку типа str
    hex_str = hash_str.hexdigest()[:10]

    # передача захешированной строки (16-теричный формат)
    hash_pwd.set(hex_str)

    # print(hex_str)
    # print(type(hex_str))

# hashing("qwerty")
# -------------------------------------------------------


# объект окна
window = Tk()
window.title("Password generator v.01")

# переменные класса StringVar
pwd = StringVar()
hash_pwd = StringVar()

# виджет (компонент) текстовой метки
Label(text="Пароль:").grid(row=0, column=0, padx=5, pady=5)

# виджет поня ввода 
Entry(textvariable=pwd).grid(row=0, column=1, padx=5, pady=5)

# виджет кнопки
Button(text="СТАРТ", command=hashing).grid(row=1, column=0, padx=5, pady=5)

# виджет поля вывода
Entry(textvariable=hash_pwd).grid(row=1, column=1, padx=5, pady=5)

# запуск программы (точка входа программы)
window.mainloop()

