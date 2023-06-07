import telebot
import random

from telebot import types

bot = telebot.TeleBot("6252956205:AAHO7_KaD_KkIQ8YNwebxtjB7yIXthRO8Fo")

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('sticker.jfif', 'rb')
    bot.send_sticker(message.chat.id, sti)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Случайное число")
    item2 = types.KeyboardButton("авав!")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, f"Приветствую, {message.from_user.first_name}". format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['вур'])
def vur(message):
    sti3 = open('i.webp', 'rb')
    bot.send_sticker(message.chat.id, sti3)
    bot.send_message(message.chat.id, "VUUUUURRRR!")

@bot.message_handler(commands=['абр'])
def abr(message):
    sti2 = open('sticker.png', 'rb')
    bot.send_sticker(message.chat.id, sti2)

@bot.message_handler(content_types=["text"])
def la(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, "привет")
    elif message.chat.type == 'private':
        if message.text == 'Случайное число':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == 'авав!':
            markup = types.InlineKeyboardMarkup(row_width=2)
            sti4 = open('sticker2.jfif', 'rb')
            bot.send_sticker(message.chat.id, sti4)
            bot.send_message(message.chat.id, "авав?!")
        else:
            bot.send_message(message.chat.id, "Error")

bot.polling()