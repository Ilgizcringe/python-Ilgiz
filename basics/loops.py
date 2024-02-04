'''================== Цикл ==================='''
# Интерация -> это прохождеегие по последовательности
# Интерируемый обьект -> обьекст по которому можно проходить, который способен возвращать элементы по одному

# цикл -> это блок кода, который повторяется несколько раз
# используется в тех случаях, когда нужно выполнить определённое действие n-ое кол-во раз или пройтись по ирерируемому обьекту

'''
Синтаксис
'''
# for пкеременная in инрерируемый_обьект:
    # код (тело цикла)

# string = 'hello world'
# # string[0] ...

# for i in string:
#     print(i) # выводим в терминал каждый элемент из последовательности

# print(i, 'последний символ') # выполнится после завершение цикла

# list_ = [1, 2, 3, 4, 5, 6]
# for element in list_:
#     print(element + 9) # к каждому элементу последовательности прибавляем 9

# for i in list_:
#     print(pow(1, 2)) # каждый элемент последовательности возводим в квадрат

# for i un (1, 2, 3, 'hello', 'py'):
#   print(i)

# for i in range(1, 101):
#   print(i) 

# ls =[]
# for i in range(1, 101):
#   print(i)
#   ls.append(i)
#   # print(ls)

# print(ls){'name' : 'test', 'password' : '123456789', 'email' : 'test@gmail.com'}

# for i in 2849: # числа не итерируемые, нельзя проходить циклом
#     print(i) 
# 'int' object is not iterable{'name' : 'test', 'password' : '123456789', 'email' : 'test@gmail.com'}

# for i in range(1, 11):
#     if i == 2:
#         print('two')
#     else:
#         print(i)

# for i in range(1, 11):
#     if i % 2:
#         print(i, 'нечетное')
#     else:
#        print(i, 'четное')

# list_ = [1, 2, 3, 4, 5, 6, 7]

# len_ = len(list_)
# print(len_)

# for i in range(len_):
#     list_.pop()

# print(list_)

# for i in range(1, 6):
#     print(i, 'i')
#     for j in range(1, 11):
#         print('hello')
#         for b in range(1, 4):
#             print('python')

'''
====================================== Цикл while ===========================================
'''
# синтаксис
# while условие:
#     тело цикла

# while True: # бесконечный цикл
#     print('hello')


# for i in range(1, 11):
#     print(i)

# counter = 0
# while counter < 10:
#     counter = counter + 1
#     counter += 1
#     print(counter)



'''
синтаксический сахар
'''

# num = 10
# num += 1 # инкремент 
# num += 3 # num = num + 3
# num -= 1 # дикремент
# num -= 6 # num = num - 6
# num *= 2 # num = num * 2
# num /= 5 # num = num / 5
# print(num)


# counter = 0
# while counter != 10:
#     counter += 1
#     print(counter)

# counter = 10
# while counter != 0:
#     counter -= 1
#     print(counter)
# print('=============')

# a = 0
# while a:
#     print('hello')
# никогда не заработает bool(0) -> False

# a = input('Введите имя: ')
# while not a:
#     a = input()


'''
========================== Итерация по словарям ==================================
'''
dict_ = {'name': 'test', 'password': '12345678', 'email': 'test@gmail.com'}

# for i in dict_: # получение значение по ключу
#     print(dict_[i])

# for i in dict_: # получаем только ключи
#     print(i)
#     print(dict_.get(1))
# for i in dict_: # получение значение по ключу
#     print(dict_[i])

# print(dict_.keys())
# for key in dict_.keys(): # получение ключей словаря
#     print(key)

# for values in dict_.values():
#    print(values)
# получение значений словаря (работает быстрее чем обращение по ключу или вызов методов get)
    
# for i in dict_.items(): # получение пар (ключ, значение)
#     print(i)
# ('name', 'test')
# ('password', '123456789')
# ('email', 'test@gmail.com')


# a, b = 'an'
# print(a) # a
# print(b) # n
# a, b, c = [1, 2, 3]
# hello, privet = ['hello', 'privet']

# for key, value in dict_.items(): # распаковываем кортежи с парами на две переменные, где переменная для ключа, а вторая для значения
#     print(f'Ключ: (key)\nЗначение: (value)')


# '1234567898765432345678'
'''бесконечный цикл for'''
# a = [1, 2, 3]
# for i in a:
#     a.append(i)
#     print(a)

# sum = 0
# num = 12345676543
# for i in str(num):
#     # print(i)
#     sum += int(i)
#     # print(int(i))
# print(sum)

num = '12345674534564324564324356432345'
sum = 0
l = 0

# while l < len(num):
#     a = num[l]
#     # print(a)
#     sum += int(a)
#     l += 1
# print(sum)

'''
========================= Ключевые слова в циклах ================================
'''
# break -> полностью выйти из цикла (прерывание цикла)
# continue -> переход к следующей интерации (к следующему прохождению, минуя оставшийся код)

# for i in range(1, 11):
#     print(i)
#     break
# 1

# for i in range(1, 11):
#     print(i)
#     if i == 7:
#         break
# # 1 2 3 4 5 6 7

# for i in range(1, 11):
#     if i == 7:
#         break
#     print(i)
# 1 2 3 4 5 6

# for i in range(1, 11):
#     if i == 3:
#         continue
#     print(i)


# for i in range(1, 11):
#     print(i)
#     if i == 3:
#         continue

# for i in range(1, 11):
#     print(i)
#     continue
#     print(hello) # никогда не заработает

# i = 0
# while i < 10:
#     i += 1
#     if i == 7:
#         continue 
#     print(i)

# i = 0
# while < 10:

#     if i == 7:
#         continue # бесконечный цикл, так как инкремент никогла не сработает и 1 не станет больше 7
#     print(i)
#     1 += 1

''' pass -> ничего не делает, выступает в роли заглушки'''
# for i in 'hello':
#     pass # просто заглушка

# for i in 'hello':
#     ... # та же самая заглушка

# num = 0
# if num == 0:
    # pass or ...

''' else в циклах'''
# else -> проверяет завершился ли цикл естественным путём ил использовалась инстукция break. Код в else сработает, если не использовался (не сработал) break 

# for i in 'hello world':
#     print(i)
#     if i == 'a':
#         break
# else:
#     print('Буквы а в строке нет')

# for i in 'hella worlda':
#     print(i)
#     if i == 'a':
#         break
# else:
#     print('Буквы а в строке нет')

list_ = ('chel', 'privet')
new_list = list_[1],list_[0]
print(new_list)
# print(list_)