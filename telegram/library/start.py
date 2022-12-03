from library import messages
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

welcome = messages.welcome + messages.options
help = messages.help + messages.options

def buttons():
    markup = InlineKeyboardMarkup(row_width = 1)
    b_profile = InlineKeyboardButton('Perfil 👤', callback_data="perfil")
    b_search = InlineKeyboardButton("Buscar 🔎", callback_data="buscar")
    b_close = InlineKeyboardButton("Cerrar 🚪", callback_data="cerrar")
    markup.row(b_profile)
    markup.row(b_search)
    markup.row(b_close)
    return(markup)
