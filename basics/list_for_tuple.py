'''
Тип данных Списки list(). Функций range(). Цикл for. Кортеж tuple()
'''

# списки - изменяемые, упорядоченные, индексируемые

# литералы -> [] (константа, выражение, которое создаёт обьект) используя "" -> создаём str, используя [] -> создаём list

'''============== Создание списков ==================='''

# 1. list_ = [] # пустой список
# 2. list1 = list('hello') # ['h','e','l','l','o']
# print(list1)

# list(iterable) -> создаёт список 

# 3. list2 = list(range(1,11))
# print(list2)

# range(start, end, step) -> возвращает последовательность элементов, если передать только end, последовательность чисел начнется с 0 и закончится до end (end не включительно)

# list_ = [1, 2, 3, 4, 'hello', True, False, ('a', 'b')]
# list_[0] # 1
# list_[4] #hello
# print(list_[4](2)) # l
# print(list_(-2)) # None
# print(list_(-1)) # ['a', 'b']
# print(list_(-1)(-1)) # b

# list_[0] = 9 # изменили элемент списка под индексом 0
# print(list_)

# a = 'hello'
# a[0] = 'l' # неправильно

# print(dir(list))

'''
================== Методы списков =====================
'''
# .append(element) -> добавляет элемент в конец списка
# list_ = [1, 2, 3]
# # print(id(list_))
# list_.append('hello')
# list_.append([4, 5, 6])
# # print(list_) # [1, 2, 3, 'hello']
# # print(id(list_))

# # .extend(iterable) -> расширяет список добавляя в конец каждый элемент iterable по отдельности
# list_= ['makers', True, False, 1.2, 99, 6]
# list_.extend('hello')
# list_.extend([1,2,3])
# list_extend(2345678) # ошибка
# print(list_)
# 2345678

# .insert(index, element) -> добаавляет element по указанному index
# list_ = [3, 4, 9]
# list_.insert(0, 'hello')
# list_[100] # ошибка
# list_.insert(100, 'world') # добавит в конец
# print(list_)

# .index(element, [start], [end]) -> возвращает индекс нашего element
# list_ = [
#     'hello', 'makers', True, 
#     False, True, None, [4, 5, 6] 
#     ]
# print(list_.index(True)) #2
# print(list_.index(True, 3, 6)) # поиски начнётся с 3 индекса и закончится на 6 индексе
# list_.index('test') # будет ошибка (так как такого элемента нет в списке)

# print(list_[-1].index(4)) #0

# .clear() -> очищает список
# list_ = [
#     'hello', 'makers', True, 
#     False, True, None, [4, 5, 6] 
#     ]
# list_.clear()
# print(list_) # []

# .count(element) -> считывает количество повторений element в списке
# list_ = [
#     'hello', 'makers', True, 
#     False, True, None, 'python', 'python','python', [4, 5, 6] 
#     ]

# print(list_.count(True)) # 2
# print(list_.count('python')) # 3
# print(list_.count('py')) # 0

# .len() -> возвращает кол-во элементов (обьектов) в списке
# print(len(list_)) #10


# .pop([index]) -> удаляет элемент из списка по идексу, если индекс не передаввать -> удаляет последний элемент списка, также вохвращает удаленный элемент

# list_ = [
#     'hello', 'makers', True, 
#     False, True, None, 'python', 'python','python', [4, 5, 6] 
#     ]

# popped = list_.pop()
# print(list_, "=========", popped)
# popped2 = list_.pop(0)
# print(list_.pop(0)) # 'hello'
# print(list_.pop(110)) # ошибка
# print(list_)

# .remove(element) -> удаляет первый принятый элемент из списка
# list_ = [
#     'hello', 'makers', True, 
#     False, True, None, 'python', 'python','python', [4, 5, 6] 
#     ]
# list_.remove('python')
# list_.remove('test') # ошибка
# print(list_)


# .reverse() -> изменяет список, переворачивает
# list_ = [1, 2, 3, 4, 5, 6]
# list_.reverse()
# print(list_)

# .sort([reverse=True]) -> сортирует список, состоящий из элемента одного типа
# list_ = [77, 3, 5, 8, 9, 'hello'] # ошибка
# list_ = [77, 3, 4, 5, 6, 9]
# list_.sort() # по возрастанию
# list_.sort(reverse=True) # по убыванию
# print(list_)

# list_ = ['hello', 'apple', 'makers', 'ab','bb']
#  list_.sort()
# print(list_)

# .copy() -> поверхностно копирует список
# list_ = ['hello', 'apple', 'makers', 'ab','bb']
# new_list = list_.copy()
# new_list.append('32')
# print(new_list)
# print(list_)

# print(dir(list))

'''====================== Кортеж  tuple============================'''
# лиьтералы -> , ()
# tuple() -> создаёт кортеж

# неизменяемый, индексируемый, упорядоченный, итерируемый
# a = (1, 2)
# print(a[0])

# .count(element) -> считывает количество повторений element в кортеже
# list_ = [
#     'hello', 'makers', True, 
#     False, True, None, 'python', 'python','python', [4, 5, 6] 
#     ]
# print(list_.count(True)) # 2
# print(list_.count('python')) # 3
# print(list_.count('py')) # 0

# .index(element, [start], [end]) -> работает также как и в списке

# # tuple_ = () # постой кортеж
# tuple_ = (3,) # кортеж с одним элементом
# tuple_ = tuple('hello')
# tuple_ = 1, 2, 3 # кортеж
# tuple_ = 1, # кортеж с одним элементом
# print(tuple_)
# # print(type(tuple_))


'''======================== Цикл =========================='''
# цикл -> это блок кода, который повторяется какое-то кол-во раз
# list_ = [1, 2, 3, 4, 5]
# list_.pop()
# list_.pop()

# for переменная in list_:
#     # тело1


# for i in list_:
#     print('работаем')
#     print(i)

# print(list_)