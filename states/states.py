from telebot.handler_backends import State, StatesGroup 



class TopState(StatesGroup):
    # Just name variables differently
    city = State()
    destinationId = State()
    hotelCount = State()
    img = State()
    imgCount = State()