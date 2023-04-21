import telebot

bot = telebot.TeleBot('5785224225:AAE_UGdBOeWS2POc7oENRxyq328rhXm41QY')


@bot.message_handler(commands=['start', 'help'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if message.text == "Привет":
            bot.send_message(message.chat.id, 'И тебе привет ёпта')
    elif message.text == "id":
            bot.send_message(message.chat.id, f"твой ID:, {message.from_user.id}")
    elif message.text == "Имя":
            bot.send_message(message.chat.id, f"твое имя, {message.from_user.first_name} опять напился?")
    else : bot.send_message(message.chat.id, f"Насяльника нэ панимаю")
bot.polling(none_stop=True)
