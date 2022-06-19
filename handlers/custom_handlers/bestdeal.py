from telebot.types import Message

from loader import bot


@bot.message_handler(commands=['bestdeal'])
def bot_bestdeal(message: Message):
	bot.send_message(message.from_user.id, "best")

