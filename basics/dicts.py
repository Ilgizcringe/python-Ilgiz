'''
Словари dict()
'''
# изменяемый, неиндексируемый, итерируемый, упорядоченный тип данных, в котором все данные хранятся в парах {ключ: значение}

# {} -> литералы

# Синтаксис
{'key': 'value'}







'''
{ключ: значение}
1. ключи в словарях должны относится к неизменяемым типам данных
2. ключи должны быть уникальными (не должны повторяться)
3. значениями в словарях могут быть любые типы данных
'''

# dict_ = {[1, 2]: 'hello'} #unhashable type: 'list'
# dict_ ={2: [1, 2]}
# dict_ = {True: 'hello', 1: '7777777', False: 7, 0: [1, 1]}
# print(dict_)



'''
Создание словарей
'''
# 1. {}
dct = {1: [1,2], 'hello': 5}

# 2. dict()
t = (('key', 'value'), ('key2', 'value2'))
# # print(dict(t))
l = [[1, 2], [6, 7]]
# print(dict(l))
l2 = [[1, 2], [6, 7]]
# print(dict(l2))
t2 = (('key', 'value'), ['key2', 'value2'])
# print(dict(t2))
# a = (('ab'), ('yh'))  
# print(dict(a))
# print(dict(a=10))

'''
====================================== Методы словарей ====================================
'''
# print(dir(dict))

# .clear() -> очищает словарь
dict_ = {'one': 1, True: [1, 2, 3, 4], None: '', 'two': 2}
# dict_clear()
# print(dict_)

# .copy() ->  возвращает копию словаря
dict_ = {'one': 1, True: [1, 2, 3, 4], None: '', 'two': 2}
# dict_2 = dict_.copy()
# print(dict_2)

# .fromkeys(seq, [value]) -> создаёт словарь с ключами из seq и значением value (для всех ключей) (по умолчанию None)
seq = ['name', 'last_name', 'age', 'email']
# dict_ = dict.fromkeys(seq, '')
# print(dict_)

# .get(key, [default]) -> возвращает значение по ключу, но не бросает ошибку если ключа нет а возвращает наш default (по умолчанию None)
dict_ = {'one': 1, True: [1, 2, 3, 4], None: '', 'two': 2}
# value1 = dict_.get(True)
# value2 = dict_.get('hello') # ошибки не будет, вернёт None
value2 = dict_.get('hello', ' Такого ключа нет') # ошибки не будет, вернёт 'Такого ключа нет'
# print(value2)
# dict_('hello') # будет ошибка, так как ключа нет

# .setdefault(key, [value]) -> 2 варианта работы

# 1. получение значение (как .get)
dict_ = {'one': 1, True: [1, 2, 3, 4], None: '', 'two': 2}
# value1 = dict_.setdefault('one')
# print(value1. '==========', dict__)

# 2. добавляет новую пару ключ: значенме в словарь (значение по умолчанию None) и возвращает значение
# value2 = dict.setdefault('hello')
# value2 = dict.setdefault('hello', 'world')
# print(value2, '===========', dict_)

# dict_ = {'one': 1, True: [1, 2, 3, 4], None: '', 'two': 2}
# dict_['one'] = 'dsakjfnjs' # изменение значения по клчу
# dict_['print'] = 'выводит в терминал' # добавили новую пару в словарь
# print(dict_)

# .update(dict_) -> добавляет в словарь наш dict_ (расширяем словарь)
person = {'name': 'John', 'last_name: ': 'Snow', 'age': 34, 'city': 'Karakol'}
person.update({'age': 24, 'hobby': ['football', 'video games']}) # если предать существующий ключ, то изменится значение у существующего ключа
# print(person)

# .values() -> возвращает все значения словаря
person = {'name': 'John', 'last_name: ': 'Snow', 'age': 34, 'city': 'Karakol'}
values_ = person.values()
# print(values())

# .keys() -> возвращает все ключи словаря
person = {'name': 'John', 'last_name: ': 'Snow', 'age': 34, 'city': 'Karakol'}
# print(person.keys())

# .items() -> возввращает пары из словаря
person = {'name': 'John', 'last_name: ': 'Snow', 'age': 34, 'city': 'Karakol'}
# print(person.items())

# .pop(key, [message]) -> удаляет пару из словаря по ключу и возваращает только значение (если ключа нет, возвращает message (если не передать message будет ошибка))
person = {'name': 'John', 'last_name: ': 'Snow', 'age': 34, 'city': 'Karakol'}
# popped= person.pop('name') # John
# popped = person.pop('mane') # ошибка
# popped = person.pop('mane', 'такого клбчва нет')
# 'такого ключа нет'
# print(person, popped)

# .popitem() -> удаляет последнюю добавленную пару, возвращает ключ и значение
person = {'name': 'John', 'last_name: ': 'Snow', 'age': 34, 'city': 'Karakol'}
# popped = person.popitem() # ('city', 'Karakol')
# print(person, '       ', popped)

list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
dict_ = {}
list1 = []
list2 = []
for i in list_:
    if type(i) == str:
        list1.append(i)
    if type(i) == int:
        list2.append(i)
    dict_ = dict(zip(list1, list2))
print(dict_)
