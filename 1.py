import telebot
import random
bot = telebot.TeleBot('5987105655:AAHj_HCCjCYgYWMObgW8mAhY4H2fiASeJ9I')

@bot.message_handler(commands=['start'])

def start(message):
    keybord = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton('Random Int', callback_data='random')
    btn2 = telebot.types.InlineKeyboardButton('Say hello', callback_data='hello')
    btn3 = telebot.types.InlineKeyboardButton('Echo', callback_data='echo')
    keybord.add(btn1, btn2,btn3)
    bot.send_message(message.chat.id, 'Select option', reply_markup=keybord)
@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.data == 'random':
        bot.send_message(call.message.chat.id, str(random.randint(1,100)))
    elif call.data == 'hello':
        bot.send_message(call.message.chat.id, f'Hello, {call.from_user.first_name}')
    elif call.data == 'echo':
        msg = bot.send_message(call.message.chat.id, 'Как тебя зовут?')
        bot.register_next_step_handler(msg, echo_func)
def echo_func(message):
    msg = bot.send_message(message.chat.id, f'Привет, {message.text} как твои дела?')
    bot.register_next_step_handler(msg, kak_dela)
def kak_dela(message):
    bot.send_message(message.chat.id, f'Я рад что у тебя {message.text}')
bot.infinity_polling()
