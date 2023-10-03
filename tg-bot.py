from telegram import Bot

# Замените 'YOUR_BOT_TOKEN' на реальный токен вашего бота
bot = Bot(token='6499447008:AAGK8nqZp1izdGU4UpzjMAzA31Bqch7MFaM')

# Замените 'YOUR_CHAT_ID' на реальный chat_id вашего канала или пользователя
chat_id = '-1001760486047'

# Отправка сообщения
bot.send_message(chat_id=chat_id, text='This test message')
