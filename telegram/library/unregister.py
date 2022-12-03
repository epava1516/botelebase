from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

message = "Date de baja como anunciante"

def buttons():
    markup = InlineKeyboardMarkup()
    b_register = InlineKeyboardButton('Registrar baja', callback_data='register')
    markup.row(b_register)
    b_back = InlineKeyboardButton("Volver 🔙", callback_data="start")
    b_close = InlineKeyboardButton("Cerrar 🚪", callback_data="cerrar")
    markup.row(b_back, b_close)
    return(markup)