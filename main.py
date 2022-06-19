from loader import bot
import handlers
from telebot import custom_filters
from utils.set_bot_commands import set_default_commands

if __name__ == '__main__':
    set_default_commands(bot)

    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.add_custom_filter(custom_filters.IsDigitFilter())

    bot.infinity_polling()
