from states.states import TopState
from loader import bot
from models import user

@bot.callback_query_handler(func=lambda call: True, state=TopState.destinationId )
def callback_query(call):
   
    data = user.get_data()
    data.set_destinationId(call.data)
    user.set_data(data)
    bot.set_state(call.from_user.id, TopState.hotelCount, call.message.chat.id)
    bot.edit_message_reply_markup(call.from_user.id,call.message.id, reply_markup = None)
    bot.send_message(call.from_user.id, "количество отелей")
