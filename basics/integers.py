# Введение в типы данных
"многострочный комментарий"
"""
многострочный
комментарий
"""
# обычный комментарий

"""Образ типов данных"""
# 1. Числовые типы данных
# a. int -> целые числа. Пример: 1,2,3
# b. flost() -> числа с плавающей точкой. Пример: 2.3,4.5 
# c. complex() -> Комплексные числа (3 + 5i/j)
# 2. Nonetype -> None пусто
# 3. Boolean -> bool() правда или ложь (True or False)
# 4. Спискаовые типы:
    # a. list() список -> массив [1,2,4,6. False. None. ...]
    # b. tuple() кортеж -> (1,2,3,4, True)
# 5. str() -> строки -> "Hello World"
# 6. set() -> множество -> {1,2,3,4,1}
# 7. frozenset() -> замороженное множество
# 8. dict() -> словарь -> {1: "one", 2: "two"...}

"""
Mutable (изменяяемые типы данных) -> можно добавлять и удалять элементы
    1. list()
    2. set()
    3. dict()
"""

"""================== Переменная =================="""
# ссылка на ячейку памяти. используется для хранения информации

# a = 4
# print(a)

"""ТАК ДЕЛАТЬ НЕЛЬЗЯ"""



# 3a = "hello" неправильно
# *a = 6 # неправильно
# a% = "неправильно"
# print = 'неправильно' нельзя использовать зарезервированные слова (те, что есть в python).

# namel = 'Ilgiz'
# nalme = 'Sam'
# name_ = 'lol'
# _name = 'wow'
# one_two = 5 #snake case
# oneTwo = 5 #camel case


'''========== Ввод =========='''
# input() -> функция ввода данных (чтобы принять от пользователя данные)
# print() -> функция вывода данных (чтобы вывести/распечатать в терминал)
			

# a = 'hello python 32'
# print(a)]

# a = int(input('Введите свой возраст'))
# print(a, 'это переменная а')

# print(type(a))
# print(type([1,2,3]))
# print(a + 9)

# type -> возвращает тип данных объекта
# int -> переводит в тип данных целые числа int()

# a = '8'
# b = int(a)
# print(type(a))

'''========== Операция над числами =========='''
# + -> сложение
# print(4 + 6)
# num1 = 4
# num2 = 88
# print(num1 + num2)

# - -> вычитание
# print(55-98)

# * -> умножение

# / -> деление (float -> 5.8)
# num1 = 454
# num2 = 88
# print(num1 / num2)

# // -> целочисленное деление -> int 
# num1 = 10
# num2 = 5
# print(num1 // num2)

# % -> получение остатка от деления
# num1 = 14
# num2 = 5
# print(num1 % num2)

# ** -> возведение в степень
# num1 = 10
# num2 = 3
# print(num1 ** num2)

# import math 

# print(math.sqrt(100))

# print(dir(math))

# math -> модуль (файл) с готовым кодом (функций, переменные, классы)
# dir -> возвращает методы, функции обьекта или модуля
# print(dir('hello'))


# a = 9
'''множественное присваивание, разом присваеваем значение несколькими переменным'''
# a, b, c = 1, 2 ,3

# abs() -> функция для нахождения модуля от числа (делает число положительным) |-42| -> 45
# print(abs(-32)) # 32
# print(abs(12)) # 12
# print(abs(-3.9)) # 3.9

# pow(x, y, z) -> 1. возводит число в определённую степень
        # 2. возвращает остаток от деления первого результата на третье число
# print(pow(5, 3)) # 5 ** 3
# print (pow(5, 3, 9)) # получили остаток от деления 5 ** 3 % 9


# divmod() -> функция принимает два числа и возвращает два числа -> первое число - результат целочислинного деления, второе число - остаток от деления

# print(divmod(99, 4)) # 99 // 4 = 24, 99 % 4 = 3 (24, 3)
# print(divmod(5, 2)) # (2,1)

# round() -> округляет число

# a = 4.534403
# print(round(a)) -> 5.5
# print(round(a, 1)) -> оставит одно число после запятой (4.5) 


import random

# print(dir(random))

# random_number = random.randint(x,y) -> рандомное число от x - y 
# random_number = random.randrange(1, 55, 2) -> 1,3,5,7,9,11
# print(random_number)
# rand = random.random() -> возвращает рандомное число от 0 до 1 -> float
# print(rand)
# print(random_rang                                