'''
Введение в функции. Аннотация
'''
'''
Аннотация - помогает сделать код информативным (подсказки)
'''
# a = 'str'
# a :int = 7
# a = 'str'

''''
================ Функции ====================
'''
# название()
# код выполняющий определенную задачу
# именованный блок кода выполняющий определенную задачу, может принимать аргументы и возвращать результат

# print('hello')


'''
синтаксис
'''
# def название_функции(параметры):
#     <тело функции>

# def -> ключевое слово, которое указывает питону что мы хотит создать функция (определить)
# <название_функции> -> по сути переменная, под которой питон запоминает функция (код)
# параметры -> переменные для функции, в которых сохраняется объект с которым будет работать функция

# def sum_two_num(x: int, y: int): #шаблон работы функции
#     print(x + y)
    

# sum_two_num('hello', '666') # вызов функции ОБЯЗАТЕЛЬНО!!!
# sum_two_num(9, 88)


def my_len(a):
    count = 0
    for i in a:
        count += 1
    print(count)
    return count

list_ = [1, 2, 3, 4, 9, 5, 3, 4, 5]

# my_len(list_)
# my_len('fgjhkl;kjhgh')
# my_len({'a': 1})
# my_len((1, 2, 3, 4, 5))
# count = 0
# for i in list_:
#     count += 1
# print(count)

# DRY -> don't repeat yourself
# Функции нужны, чтобы избежать повторение кода и соблюcти принцип dry


# a = 'string'.replace('s', 'H')
# print(a)
# result = my_len(list_)
# print(result)

'''return'''
# используется для возвращения результата, в дальнейшем этот результат можно сохранить в переменной и работать с ним
# return -> говорит о заврешении функции

# def sum_(x: int, y: int):
#     return x + y # после return код не читается
#     print('==========') # никогда не сработает


# print(sum_(9, 99))
# res = sum_(45, 50)
# print(res)
    
# def sum_():
#     return 8 + 9
# print(sum_())
# print(sum_())
# print(sum_())
    

''' Параметры и аргументы '''
# параметры -> переменные внутри функции, указываются при определении (def) функции в скобках
# аргументы -> значение, которые передаем параметрам при вызове функции


'''
======================= Виды параметров =========================
'''
# 1. обязательные (x, y, a, name ...) -> определяют, какие аргументы нужно передать при вызове функции (при этом нужно передовать столько аргументов, столько и параметров)
# 2. не обязательные (опциональные)
    # 2.1 с дефолтом (предается значение по умолчанию, которое будет использоватья, если ползователь не предал значение (аргумент) при вызове функции)
    # 2.2 args -> tuple (все лишние позиционные аргументы (без названия))
    # 2.3 kwargs -> -> dict (все лишние именованные аргументы (с названием))

'''
====================== Виды аргументов =======================
'''
# 1. позиционные (по позиции/порядку)
# 2. именованные (по названию или имени параметра/переменной (x=7, y=99))

def func(a, b): 
    print(f'обязательные параметры a, b -> a={a} b={b} ')

# func(4, 'hello') #позиционные аргументы a=4, b='hello'
# func('hello', 4)
# func() # если не передать значения для параметров при вызове -> будет ошибка TypeError: func() missing 2 required positional arguments: 'a' and 'b'
    
def func(a, b=5):
    print('обязательный параметр a -> ', a)
    print('необязательный параметр (с дефолтом) b -> ', b)

# func('test_a', [1, 2, 3]) # для параметра b задали новое значение -> [1, 2, 3]
# func('test_a') # для параметра b используется значение по умолчанию -> 5

# def pop(index_=-1):
#     pass
    
# func(b='param b', a=8) # именованные аргументы


# def func(a, b, *args, **kwargs):
#     print(a, b)
#     print(args)
#     print(kwargs)


# func(8, 5, 6, 2, 5,6, 'hello', c=99, j=88)

# print(*range(10))
# dict_ = {'one': 1, 'two': 2}
# print({*dict_}) 
# dict(one=1)
# print('hello')
    
# def test(a: int) -> str: # функция возвращает строку
#     if a % 2:
#         return 'нечетное'
#     return 'четное'

# print(test(77))

# def test(a: int) -> None: #функция по умолчанию возвращает None
#     if a % 2:
#         print('нечетное')
#     else:
#         print('четное')

# a = test(87)
# print(a)
        










'''ФАКТОРИАЛ'''

# 5! = 1*2*3*4*5

# def count_factorial(a: int) -> int:
#     fact_ = 1
#     for i in range(1, a+1): # 1, 2, 3, 4, 5
#         fact_ *= i
#     return fact_
# print(count_factorial())


db = [
    {'username': 'qwerty', 'password': hash('123456789')},
    {'username': 'admin', 'password': hash('ladmin')}
]

def register(username: str, password: str, password_confirm: str) -> str:
    for user in db:
        if user['username'] == username:
            raise ValueError('такое имя пользователя не существует')
    if password != password_confirm:
        raise ValueError('Пароли не совпадают')
    new_user = {'username': username, 'password': hash(password)}
    db.append(new_user)
    return "Вы успешко зарегестрированы"

# print(register('qwerty1', '123456789', '123456789'))
# print(db)

def login(username: str, password: str) -> str:
    for user in db:
        a = False
        if user['username'] == username and hash(password) != user['password']:
            raise Exception('не верный  пароль')
        return 'Вы успешно залогинились'
    raise Exception('Пользователь не найден')
# print(login('qwerty', '123456789'))

def main():
    while True:
        action  = input('1, register\n2, login\n3, quit')
        try:
            if action == '1':
                username = input('Введите имя пользователя; ')
                password1 = input('Введите пароль; ')
                password2 = input('Введите подтверждение паролья; ')
                register(username, password1, password2)

            elif action == '2':
                username = input('Введите имя пользователя; ')
                password1 = input('Введите пароль; ')
                login(username, password1, password2)


            elif action == '3':
                break
        except Exception as e:
            print(e)

main()