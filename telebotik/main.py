import telebot
import random

token = '6885194931:AAGhcK1OYGTNW0k5pcYxYXetyTKufb1uzC0'


bot = telebot.TeleBot(token)

# print(dir(bot))

# @bot.message_handler(commands=['start','а это теребонить тебя не должно','privet'])
# def start_message(message):
#     # print(message)
#     bot.send_message(message.chat.id, 'WASSSSSSSSUP NIGGA')
#     bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAELSeFlukVXwejNwWoYa-TZFSi_RhRpCwACFBQAApkjGEgw6f6rmz_FCjQE')

Keyboard = telebot.types.ReplyKeyboardMarkup()

button1 = telebot.types.KeyboardButton('Да')
button2 = telebot.types.KeyboardButton('Нет')
Keyboard.add(button1, button2)


@bot.message_handler(commands=['start'])
def start_message(message):
    answer = bot.send_message(message.chat.id, 'Привет, начнём игру?', reply_markup=Keyboard)
    # print(answer)
    bot.register_next_step_handler(answer, check_answer)


def check_answer(answer):
    if answer.text == 'Да':
        bot.send_message(answer.chat.id, 'YOOOO WASSSSUP BROOO\nУгадай число челлл, you have 3 chance')
        random_number = range.choice(range(1,11))
        # print(random_number)
        game(answer, 3, random_number)
    else:
        bot.send_message(answer.chat.id, 'you are not my nigga brooos') 


def game(message, attemps, random_number):
    answer = bot.send_message(message.chat.id, 'Choose int in range 1-10')
    bot.register_next_step_handler(answer, check_number, attemps-1, random_number)


def check_number(answer, attemps, random_number):
    if answer.text == str(random_number):
        bot.send_message(answer.chat.id, 'good')
        
    elif attemps == 0:
        bot.send_message(answer.chat.id, 'you have not chance')

    else:
        bot.send_message(answer.chat.id, f'not good, you have {attemps} chance')
        game(answer, attemps, random_number)


bot.polling()

