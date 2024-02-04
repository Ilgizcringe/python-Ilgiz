'''
1) Создайте список list_ из нечётных целых чисел в промежутке от 1 до 50. Нужно использовать comprehension
'''
# list_ = [i for i in range(1,50) if i % 2 != 0]
# print(list_)

'''
2) Создайте список list_ из квадратов всех чисел от 1 до 25 (включительно). Нужно использовать comprehension.
'''
# list_ = [i ** 2 for i in range(1, 26)]
# print(list_)

'''
3) Опишите полный синтаксис конструкции try-except
'''
# try: 
#     pass 
# except Exception: 
#     pass 
# else: 
#     pass 
# finally: 
#     pass

'''
4) Напишите программу, которая будет получать через input 2 числа num1, num2 и будет печатать их сумму.
Обработайте ошибку, которая возникнет, если пользователь введёт что-то кроме числа и выведите сообщение, например:
'''
# try:
#     num1 = int(input('first: '))
#     num2 = int(input('ssecond: '))
#     res = num1 + num2
#     print('sum: ', res)
# except ValueError:
#     print('Error')

'''
5) Создайте функцию divide() которая должна принимать 2 числа и возвращать результат их деления
'''
# def divide(k, v):
#     if v == 0:
#         return 'not'
#     return k // v
    
# print(divide(23,2))

'''
6) Создайте функцию:
is_palindrome()
которая будет принимать строку и проверить является ли она палиндромом.
Палиндро́м, пе́ревертень — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях. Например, число 101; слова "кок", "топот", "комок" и т.д.
Функция должна возвращать True или False. Нужно учитывать пробелы и регистр
'''
# def is_palindrome(string):
#     string = string.lower().replace(' ','')
#     return string == string[::-1]



# def is_palindrome(input_str):
#     cleaned_str = ''.join(input_str.split()).lower()
    
#     return cleaned_str == cleaned_str[::-1]

# user_input = input("Введите строку: ")
# result = is_palindrome(user_input)

# if result:
#     print(True)
# else:
#     print(False)