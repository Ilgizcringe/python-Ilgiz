'''
строки str()
'''
# неизменяемый тип данных, преднозначен для хранения текста (последовательности символов), всегда заключается в кавычки

string1 = 'строка с одинарными кавычками, внутри нельзя использовать одинарные кавычки'
string2 = "строка с двойными кавычками, внутри нельзя использовать двойные кавычки"
# string3 = "неправильная строка' # ошибка
string4 = '''
здесь можно использовать любые кавычки
и переносить текст на следующую строку
'''
string5 = """
здесь можно использовать любые кавычки
и переносить текст на следующую строку
"""


# len() -> возвращает кол-во символов в строке (длину строки)

# print(len(string5)) # пробелы тоже считаются за символы

# hello = 9
# hello
# 'hello'


'''
========== Экранированные последовательности ==========
'''
# это последовательность начинающаяся с символа "\"

'''
экранизация строк
'''
'\n' # перенос строки
'\t' # табуляция (Tab)
'\'' # отображение '
'\"' # отоброжает "
'\\' # отоброжает \
'\r' # возвращает каретку в начало строки
'\v' # перенос строки на новую линию со смещением вправо на длину предыдущей строки
'\a' # гудок встроенного системного динамика(не работает)

# print('hello \nworld')
# print('hello \tworld')
# print('\'hello world\'')
# print("\"hello world\"")
# print('hello world \\')
# print('hellofcogf \rworld')
# print('hello000000\vworld')


# + -> объединение строк (канкатенация строк, склеивание строк)

# a = 'hello'
# b = 'privet'
# print(a + ' ' + b) # hello privet

# * -> дублирование строк
# print('hello' * 3)

'''================= Индекс ================='''
# порядковый номер элементов в строке

# 'hello world'
# 012345678910
#           -1 обратно  
# str = 'hello world'
# print(str[0])
# print(str[5])
# print(str[10])

'''================= срез ================='''
# нахождение подстроки в строке

# str = 'makers bootcamp'
# print(str[0:6]) -> до 6го элемента
# print(str[:6]) -> часть строки 'makers'
# print(str[:]) -> вся строка
# print(str[7:11]) ->
# print(str[7:]) ->
# print(str[4:9]) ->

# [start:end:step]
# print(str[::2])

# print(str[::-1]) перевернули строку

# срез -> нахождение подстроки [stert: stop: step], начиная от start заканчивая до end (end не включительно) (step по умолчанию 1) (записывается каждый элемент строки)
# [1:] -> начинаем с элемента под первым индексом и до конца
# [:4] -> начинаем с 0го ндекса и до 4 (4 не включительно)
# [4:7] -> начинаем с 4го индекса и до 7 (7 не включительно)
# [::], [:], [0::1] -> получаем всю строку



'''========== Методы =========='''
# str.lstrip()
# str.split()

# .lstrip -> удаляет пробелы в левой части строки (вначале)
# a = '                          hello'
# print(a)
# print(a.lstrip())


# .rstrip() -> удаляет пробелы в правой части (в конце)
# a = 'hello      '
# print(len(a))
# print(len(a.rstrip))

# .strip() -> убирает пробелы вначале и в конце строки

# .split(разделитель) ->  разделяет строку по разделителю и возвращает тип данных списки, если разделитель не указать будет делить по пробелу
# a = 'hello, world, makers, bootcamp..'
# b = a.split() #['hello,', 'world,', 'makers,', 'bootcamp..']
# c = a.split(',') #  ['hello', ' world', ' makers', ' bootcamp..']
# d = a.split('o') 
# print(d)    


'''Методы на is -> проверяют и возвращает True/False'''
# .isdigit() -> состоит ли строка только из чисел
# .isalpha() -> состоит ли строка только из букв
# .isalnum() -> состоит ли строка только из букв и чисел
# .islower() -> состоит ли строка из символов в нижнем регистре
# .isupper() -> состоит ли строка из символов в верхнем регистре
# .isspace() -> состоит ли строка из неотображаемых символов (пробел, экранированные последовательности '\n', '\t'.....) 
# .istitle() -> наичнается ли каждое слово в строке с верхнего регистра (все остальные символы должны быть в нижнем регистре)

# str = 'hello'
# print(str.islower()) #true

# str2 = '1234567778'
# print(str2.isdigit()) #true
# ...

# .lower() -> переводит символы в нижний регистр (возвращает строку в нижний регистр)
# str1 = 'HALLO Hello heLLOOO'
# new_str = str1.lower()
# print(str1, '->', new_str)


# .upper() -> переводит символы в верхний регистр (возвращает строку в верхний регистр)
# str1 = 'HALLO Hello heLLOOO'
# new_str = str1.upper()
# print(str1, '->', new_str)

# .swapcase() -> переводит в противоположный регистр
# str1 = 'PyThOn 32 MakeRs'
# print(str1.swapcase()) 
# .title -> переводит первую букву каждого слова в верхний регистр, а все остальные в нижний
# str = 'привет рЕБЯТА' 
# new_str = str_.title()
# print(new_str)

# .capitalize() -> переводит первый символ каждой строки в верхний регистр
# str__ = 'hello world. привет'
# print(str__.capitalize())

# .replace(old, new, [count]) -> заменяет old на new если указать count, то только указанное кол-во раз


# .find(value, [start], [end]) -> возвращает индекс value (если value нет в строке вернет -1)
# str_1 = 'hello world'
# print(str_1.find('l', 4, 7))  
# print(str_1.find('world'))

# .index(substring, [start], [end]) -> возвращает индекс substring

# str___ = 'hello world'
# print(str___.index('l',3))
# print(str___.index('u')) # ошибка

# .startswith(substrig) -> проверяет, начинается ли строка с substring
# str09 = 'hello world'
# print(str09.startswith('h')) #True
# print(str09.startswith('hello')) #True
# print(str09.startswith('world')) #False
# print(str09.startswith('world', 6)) #True

# .endswith(substrig) -> проверяет, заканчивается ли строка с substring
# str09 = 'hello world!'
# print(str09.endswith('d')) #True
# print(str09.endswith('world')) #False
# print(str09.endswith('world!')) #True

# .count(substring) -> считает кол-во вхождений substring в строке

# .zfill(width) -> делает длину строки равной width, по необходимости недостоющие символы заполняет нулями
# str12_= 'hello' 
# print(str12_.zfill(6))




# 'разделитель'.join(interable/список) -> обьеденяет элементы iterable в строку используя разделитель

# list_ = ['hello', 'world', 'python', 'py32']
# print('-->'.join(list_)) # hello-->world-->python-->py32

'''============================= Форматирование строк (динамические строки) ============================='''
# inp = input('Введите имя: ')
# a = 'Привет, inp'
# print(a) #неправильно

# # %
# a = 'Привет, %s' %inp
# print(a)

# inp1 = input('Введите имя: ')
# inp2 = input('Введите фамилию: ')

# a = 'Привет, {} {}', format(inp1, inp2)
# print(a)

# f-строка -> итерполяция строк
# inp1 = input('Введите имя: ')
# inp2 = input('Введите фамилию: ')

# a = f'Привет, {inp1} {inp2}'
# print(a)
