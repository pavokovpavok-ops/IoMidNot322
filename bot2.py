import telebot

bot = telebot.TeleBot("8290804480:AAFOTgeULH3arvmWyt8_GXKW3ymyoSbpyto")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram-бот экологии! Напиши команду /hello, чтобы начать!")


@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела? 🙂")


@bot.message_handler(commands=['super'])
def send_super(message):
    bot.reply_to(message, "Молодец! Радость — это здорово! 🌿")


@bot.message_handler(commands=['ecology'])
def send_ecology(message):
    bot.reply_to(message, "Береги природу! Начни сортировать мусор, не выбрасывай его где попало и сдавай пластик на переработку. ♻️")


@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи и чистой экологии! 👋")


bot.polling()

