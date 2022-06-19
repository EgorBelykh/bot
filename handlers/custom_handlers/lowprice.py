from telebot.types import Message
from states.states import TopState
import loader
from loader import bot
from keyboards.inline import image, destination
from models import user

@bot.message_handler(commands=['lowprice'], state=None)
def bot_lowprice(message: Message):
	bot.set_state(message.from_user.id, TopState.city, message.chat.id)
	bot.send_message(message.from_user.id, "Укажите город")
	user.set_data(user.User())
	


@bot.message_handler(state=TopState.city)
def city(message: Message):
	bot.set_state(message.from_user.id, TopState.destinationId, message.chat.id)
	bot.send_message(message.from_user.id, "Уточните район", reply_markup=destination.gen_markup(loader.location(message.text)))
	data = user.get_data()
	data.set_city(message.text)
	user.set_data(data)

@bot.message_handler(state=TopState.hotelCount)
def hotel_count(message: Message, is_digit=True):
	bot.send_message(message.from_user.id, "Показать фото?", reply_markup=image.gen_markup())
	bot.set_state(message.from_user.id, TopState.img, message.chat.id)
	data = user.get_data()
	data.set_hotel_count(message.text)
	user.set_data(data)

@bot.message_handler(state=TopState.imgCount)
def img_count(message: Message, is_digit=True):
	bot.send_message(message.from_user.id, "moments.....")
	data = user.get_data()
	data.set_img_count(message.text)
	user.set_data(data)
	loader.get_property(message, data.destinationId,data.hotelCount, data.imgCount)
	bot.delete_state(message.from_user.id, message.chat.id)