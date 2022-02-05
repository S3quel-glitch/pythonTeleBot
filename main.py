import telebot
from telebot import types

bot = telebot.TeleBot('{your API-key here}')

#####THIS PART IS UNDER CONSTRUCTION#####
@bot.message_handler(commands=['text'])
def mess(message):
    get_message_bot = message.text.strip()
    print(get_message_bot)
    if get_message_bot == "start":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)  # Creating method with buttons
        btn1 = types.KeyboardButton('start')
        btn2 = types.KeyboardButton('help')
        markup.add(btn1, btn2)  # Creating buttons
        if message.from_user.last_name == None:
            send_mess = f"<b>Привет {message.from_user.first_name}</b>\nКак дела?"
            bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
        else:
            send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>\nКак дела?"
            bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "help":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)  # Creating method with buttons
        btn1 = types.KeyboardButton('start')
        btn2 = types.KeyboardButton('help')
        markup.add(btn1, btn2)  # Creating buttons
        bot.send_message(message.chat.id, 'Список доступных команд', parse_mode='html')
        bot.send_message(message.chat.id, '1.Start (Поздороваться с ботом)\n2.Help (вызвать окно справки)', parse_mode='html', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Что-то пошло не так.', parse_mode='html')

#####THIS PART IS UNDER CONSTRUCTION#####


@bot.message_handler(commands=['help'])
def show_comm(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)  # Creating method with buttons
    btn1 = types.KeyboardButton('start')
    btn2 = types.KeyboardButton('help')
    markup.add(btn1, btn2)  # Creating buttons
    bot.send_message(message.chat.id, 'Список доступных команд', parse_mode='html')
    bot.send_message(message.chat.id, '1.Start (Поздороваться с ботом)\n2.Help (вызвать окно справки)', parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3) #Creating method with buttons
    btn1 = types.KeyboardButton('start')
    btn2 = types.KeyboardButton('help')
    markup.add(btn1, btn2) #Creating buttons
    if message.from_user.last_name == None:
        send_mess = f"<b>Привет {message.from_user.first_name}</b>\nКак дела?"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
    else:
        send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>\nКак дела?"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

bot.polling(none_stop=True)
