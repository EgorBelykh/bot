from telebot.types import Message

from loader import bot


@bot.message_handler(commands=['highprice'])
def bot_highprice(message: Message):
	bot.send_message(message.from_user.id, "high")

