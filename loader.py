import telebot
from telebot import TeleBot, types
from telebot.storage import StateMemoryStorage
from config_data import config
from models.rapidAPI import Hotel, Entitie
import requests
import json


storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)

headers = {
	"X-RapidAPI-Key": config.RAPID_API_KEY,
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

def location(city):
	CITY_GROUP = []

	querystring = {"query":city,"locale":"ru_RU","currency":"RUB"}
	response = requests.request("GET", config.url_location, headers=headers, params=querystring)
	per_dict = json.loads(response.text) 
	suggestions = per_dict["suggestions"]
	for item in suggestions:
		group = item['group']
		entities = item['entities']
		for entity in entities:
			ent = Entitie(entity['caption'], entity['destinationId'], entity['name'], entity['type'])
			if group == "CITY_GROUP":
				CITY_GROUP.append(ent)
			else: 
				break
	return CITY_GROUP



def property(destinationId, price, count):
	querystring = {"destinationId":destinationId,"pageNumber":"1","pageSize":count,"checkIn":"2020-01-08","checkOut":"2020-01-15","adults1":"1","sortOrder":price,"locale":"ru_RU","currency":"RUB"}
	response = requests.request("GET", config.url_properties, headers=headers, params=querystring)
	per_dict = json.loads(response.text) 
	if(per_dict['result'] == 'OK'):
		data = per_dict['data']
		result = data['body']['searchResults']['results']
		prop = []
		for item in result:
			try:
				prop.append(Hotel(item['id'], item['name'],item['starRating'], item["ratePlan"]["price"]["current"], item['address']['streetAddress'],item['landmarks'][0]['distance']))
			except KeyError:
				id = item['id']
				print(f'{destinationId}, {id}')	
		return prop
	elif (per_dict['result'] == 'ERROR'):
		return "ERROR"

	return "ERROR"

def image(id, count):
	querystring = {"id":id}
	response = requests.request("GET", config.url_photo, headers=headers, params=querystring)
	per_dict = json.loads(response.text) 
	img_data = [] 
	try:
		images = per_dict['hotelImages']
	except KeyError:
		print(id)
	for i in range(int(count)):
		if i == len(images):
			break
		item = images[i]['baseUrl']
		#print(item)
		item = item.replace('{size}','z')
		#print(item)
		img_data.append(item)

	return img_data

def get_property(message, destinationId, hotelCount, imgCount):
	prop = property(destinationId, "PRICE", hotelCount)

	if len(prop) == 0 or prop == "ERROR":
		bot.send_message(message.chat.id, 'ERROR')
		return

	text = ''

	for item in prop:
		text = f'{item.name}\nАдрес:{item.address}\nЦена:{item.price}\nРейтинг:{item.starRating}\nРастояние до центра города:{item.landmark}'
		bot.send_message(message.chat.id, text)
		photos = image(item.id, imgCount)
		media = []
		for photo in photos:
			media.append(types.InputMediaPhoto(photo))
		try:
			bot.send_media_group(message.chat.id,media=media)
		except telebot.apihelper.ApiTelegramException:
			for photo in photos:
				try:
					bot.send_photo(message.chat.id,photo=photo)
				except telebot.apihelper.ApiTelegramException:
					print(photo)