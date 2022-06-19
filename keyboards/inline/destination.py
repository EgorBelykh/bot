from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def gen_markup(suggestions):
    markup = InlineKeyboardMarkup()
    for item in suggestions:
    	markup.add(InlineKeyboardButton(item.name, callback_data=item.destinationId))
    return markup