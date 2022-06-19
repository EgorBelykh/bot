from states.states import TopState
from loader import bot
import loader
from models import user

@bot.callback_query_handler(func=lambda call: True, state=TopState.img )
def callback_query(call):
    bot.delete_state(call.from_user.id, call.message.chat.id)
    data = user.get_data()
    if call.data == "cb_yes":
        bot.set_state(call.from_user.id, TopState.imgCount, call.message.chat.id)
        bot.send_message(call.from_user.id, "Сколько фотографий?")
        data.set_img = True
    elif call.data == "cb_no":
        bot.send_message(call.from_user.id, "секунду...")
        data.set_img = False
        loader.get_property(call.message, data.destinationId,data.hotelCount,0)
        bot.delete_state(call.from_user.id, call.message.chat.id)
    bot.edit_message_reply_markup(call.from_user.id,call.message.id, reply_markup = None)
    user.set_data(data)