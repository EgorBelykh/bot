import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
RAPID_API_KEY = os.getenv('RAPID_API_KEY')

url_location = "https://hotels4.p.rapidapi.com/locations/v2/search"
url_properties = "https://hotels4.p.rapidapi.com/properties/list"
url_photo = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"

DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку"),
    ('lowprice', "top"),
    ('highprice',"high top"),
    ('bestdeal',"best"),
    ('history',"history")
)
