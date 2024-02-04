'''
JSON (JavaScript Object Notation) -> единный текстовый формат передачи данных между компьютерами, сервисами, приложениями в интернете, (для взаимодействия backend и frontend)
'''

# {
#     "id": 1, 
#     "author": "John",
#     "posts": null
# } -> JSON

'''
Разница типов данных
'''
# Python        JSON
# dict          Object
# list          array
# tuple         array
# str           string
# int           number
# True          true
# False         false
# None          null



import json
# модуль для работы с JSON


# Сериализация (запись/перевод в JSON) -> перевод python обьекта в JSON 

# dump() -> метод, записывает python обьект в JSON файл
# dumps() -> метод, записывает python обьект в JSON строку


# Десериализация -> (Чтение данных в формате json) -> переводит JSON в Python обьект

# load() -> метод, который счиывает файл в формате JSON и переводит его в обьект python 
# loads() -> метод, который счиывает строку в формате JSON и переводит в python обьект


# person = '{"name": "Tima", "age": 26, "is_student": false}'
# print(person)
# result = json.loads(person)
# print(result)


# with open('test.json', 'w+') as file:
#     person = '{"name": "Tima", "age": 26, "is_student": false}'
#     file.write(person)
#     file.seek(0)
#     data = json.load(file)
#     print(data)
#     print(data['age'])


# person = {'name': 'Tima', 'age': 26, 'is_student': False}

# json_ = json.dumps(person)
# print(json_)
# print(type(json_))

# person = {'name': 'Tima', 'age': 26, 'is_student': False}
# with open('test.json', 'w') as file:
#     json.dump(person, file)
#     file.seek(0)
#     print(file.read())


'''
CSV -> файл CSV, файл который позволяет структурировать большие обьемы данных. Очень похож на Excel
(Comma Separated Values) -> значения, разделенные запятой
'''


# with open('data.csv', 'w') as file:
#     file.write('id, name, email')
    
# import csv 

# with open('data.csv', 'a') as file:
#     writer = csv.writer(file)
#     writer.writerow([1, 'John','johnsnow@gmail.com'])


# import lesson # импортируем весь модуль(файл), все переменные, функции ... будут доступны через название модуля
# lesson.test_module_func()
# print(lesson.lesson)

# from lesson import lesson # импортируем только нужную переменную из указанного модуля, остальное не доступно
# print(lesson)

# from lesson import * # импортируем весь модуль(файл), все переменные, функции ... будут доступны по своему имени (названию)
# f1
# lesson
# test_module_func()


'''
Модуль -> файл, который содержит код, Название файла без расширения (.py) -> название модуля
'''

# from my_package.lol import lol1, say_hello  

# from my_package import mom

# from my_package.mom import *

# mom.sum_(100,20)
# print(lol1)
# say_hello()