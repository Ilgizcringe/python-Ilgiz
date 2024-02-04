'''
Области видимости и пространства имен
'''

# Области видимости определяет, когда и где мы можем использовать свои переменые, функции.

# пространства имён -> совокупность определенных имен в настоящее время (можно представить в виде словаря("навание переменной": "значение"))

# 4 типа пространств имен

# 1. Duiltins (встроенные) -> Всё что есть в стандартной библиотеке python (print, len, list, dict, int, dir ...)

# 2. Global -> имена, которые мы обьявляем в файле (num)
# num = 0

# 3. Enclosed (не локальные) -> пространство между двух пространств

# 4. Local (локальные) -> последнее пространство
# def test(a)
#   print(a)
# a


# print(dir(__builtins__)) -> список со встроенными именами (функции, классы, переменные)


string = 'hello'
list_ = [1, 2, 3, 4, 5]

#  globals() -> возвращает словарь всех глобальных переменных (имен), где ключ -> название переменной, значение -> обьект
# print(globals())

# print(globals()['list_'])


# локальные переменные -> переменные внутри функции 

def func():
    local_a = 9 # ljcnegyj njkmrj dyenhb aeyrwbb
    print(locals())

# func()
# print(globals()) # имя local_a не появилось, так как находится в другом пространстве имен 
    
# locals() - возвращает все локальные переменные в виде словаря


# def some_func1():
#     x = 'это enclosed переменная'

#     def some_func2():
#         x = 'это локальная переменная'

#     some_func2()
#     print(x)

# some_func2() -> не доступна
# some_func()
    

# def func(test):
#     #enclose(пространство)
#     a = 'func'
#     def inner_func(test2):
#         # local пространство
#         a = 'inner_func'
#         print('Локальное пространство', locals())
#     inner_func(5)
#     print('Замкнутое (enclosed) пространство', locals())

# func(8)
    
# def test():
#     a = 0
#     b = 99


# поряд поиска имен 
    
# Local -> Enclosed -> Global -> Builtins
    

# a = 99

# def func():
#     print(a)


# a = 99

# def func():
#     # a = 'test'
#     print(a)

#     def inner_func():
#         a = 8
#         print(a, 'local')
    
#     inner_func()

# func()
    

# мы не может просто изменить значение глобальной переменной в локальном или enclosed пространствах (вызывается исключение)
# i = 0
# def func():
#     i+= 1
#     print(i)

# func()
    
# global -> позволяет менять значение глобальной переменной, находясь в локальной области 
# i = 0
# def func():
#     global i
#     i+= 1

# func()
# print(i)
    

# count = 0

# def counter():
#     global count
#     count += 1
#     return count

# print(counter())
# print(counter())
# print(counter())
    
# test_value = 9

# def func():
#     global test_value 
#     test_value += 1 # 10
#     def inner_func():
#         global test_value # меняем второй раз значение глобальной переменной
#         test_value = 'hello'
#     inner_func()

# func()
# print(test_value) # hello



'''
изменение enclosed переменной
'''

# def func():
#     a = 0
#     def inner_func():
#         nonlocal a # доступ на изменение enclosed переменной в локальной области
#         a += 1
#     inner_func()
#     print(a)

# func()


# import this
