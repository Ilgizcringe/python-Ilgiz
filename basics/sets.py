'''
Множества set()
изменяемый, неупорядоченный, неиндексируемый, итерируемый имп данных
Предназначен для хранения уникальных значений (ТОЛЬКО НЕИЗМЕНЯЕМЫЕ ТИПЫ ДАННЫХ)
'''
set1 = {1, 2, 3, 4}
set2 = {1, 1, 1, 1, 2, 3, 4, 'hello', 'python', 'a'}
# set3 = {([1, 2,], 'hello')} 1) #если передаём tuple, то он тоже должен состоять только из неизменяемых типов
set4 = {0, False, True, 1}
# print(set4)


'''
Создание множество
'''
# 1. set()
# set_ = set([8, 9, 7])
# set_ = set({'one': 1, 'two': 2}) # во множество запишутся только ключи
# set_ = set('hello world')
# print(set_)

# set_ = {} # пустое множество
# print(type(set_))
# set_ = set() # пустое множество
# print(type(set_))

# 2. {}
# set_ = {'hello', 'a', 'p', 'makers'}
# print(set_)

'''
Методы множества
'''
# добавление элементов во множество
# .update(seq)
# .add(element)
# set_ = {'hello', 'a', 'p', 'makers'}
# set_.update([1, 2 ,3, 'python', 1]) # расширяет множество, добавляя элементы из итерируемого обьекта (элементы не дублируются)
# print(set_)

# .addle(element)
# set_ = {'hello', 'a', 'p', 'makers'}
# set_.add{[1, 2, 3]} # SyntaxError: invalid syntax: 'list' можно добавитьтолько неизменяемые типы данных
# set_.add('name')
# set_.add(False)
# set_.add(('hello', 1, None))
# print(set_)


# .copy() -> возвращает копию множества
# .clear() -> очищает множество

# .remove(element) -> удаляет элемент из множества, если передать не существущий обьект выдаст ошибку
# set_ = {'hello', 'a', 'p', 'makers'}
# set_.remove('hello')
# set_.remove(1) #KeyError: 1
# print(set_)

# .discard(element) -> удаляет элемент из множества, но если такого элемента нет то не выдаёт ошибку
# set_ = {'hello', 'a', 'p', 'makers'}
# set_.discard('a')
# set_.discard(1) # ошибку не выдаёт
# print(set_)

# .pop() -> удаляет и возвращает случайный элемент из множества (первый из сформированной последовательности)
# set_ = {'hello', 'a', 'p', 'makers'}
# print(set_)
# set_.pop()
# set_.pop()
# print(set_)


# set_a.differens(set_b) -> выведет элементы которые есть в set_a но нет в set_b (уникальные элементы первого множества)
# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}
# print(set_a.differens(set_b)) #{1, 2}
# set_a . set_b


# set_a.symmetric_difierence(set_b) -> возвращает уникальные элементы set_a и set_b (то есть элементы не повторяющиеся в обоих множествах)
# set_a = {9, 0, 7, 4, 6, 4}
# set_b = {1, 3, 6, 5, 8, 9}
# print(set_a.symmetric_difference(set_b))
# set_a ^ set_b

# set_a.intersection(set_b) -> возвращает схожие элементы обоих множеств
# set_a = {9, 0, 7, 4, 6, 4}
# set_b = {1, 3, 6, 5, 8, 9}
# print(set_a.intersection(set_b))
# print(set_a & set_b)

# set_a.union(set_b) -> обьединяет элементы обоих множеств
# set_a = {1, 2, 3, 4, 5, 6}
# set_b = {3, 4, 5, 6, 7, 8}
# print(set_a.union(set_b))
# print(set_a | set_b)


# Д.З
# .difference_update()
# .intersection_update()
# .symmetric_difference_update()
# .isdisjoint()
# .issubject()
# .issuperset()

