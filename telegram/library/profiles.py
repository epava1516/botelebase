import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup, ForceReply

response = requests.get('http://localhost:8000/api/users/')
lista = response.json()

class profileHandler:
    def __init__(self):
        # self.searchResponse = search_json
        self.message = "Crea tu perfil para poder ajustar los resultados de tus busquedas o para empezar a anunciarte.\n\n"

    def buttons(self):
        markup = InlineKeyboardMarkup()
        b_username = InlineKeyboardButton('Nombre publico', callback_data='e_username')
        b_photos = InlineKeyboardButton('Fotos', callback_data='e_fotos')
        b_name = InlineKeyboardButton('Nombres', callback_data='e_nombres')
        b_lastname = InlineKeyboardButton('Apelidos', callback_data='e_apellidos')
        b_description = InlineKeyboardButton('Descripción', callback_data='e_descripcion')
        b_nationality = InlineKeyboardButton('Nacionalidad', callback_data='e_nacionalidad')
        b_age = InlineKeyboardButton('Edad', callback_data='e_edad')
        b_genre = InlineKeyboardButton('Genero', callback_data='e_genero')
        b_phone = InlineKeyboardButton('Teléfono', callback_data='e_telefono')
        b_email = InlineKeyboardButton('Email', callback_data='e_email')
        b_dni = InlineKeyboardButton('DNI o Pasaporte', callback_data='e_dni')
        b_direccion = InlineKeyboardButton('Localización', callback_data='e_localización')
        b_register = InlineKeyboardButton('Hazte anunciante ⬆️', callback_data="alta")
        b_unregister = InlineKeyboardButton("Hacer perfil privado ⬇️", callback_data="baja")
        b_back = InlineKeyboardButton("Volver 🔙", callback_data="start")
        b_close = InlineKeyboardButton("Cerrar 🚪", callback_data="cerrar")
        markup.row(b_username)
        markup.row(b_photos)
        markup.row(b_name, b_lastname)
        markup.row(b_description, b_nationality)
        markup.row(b_age, b_genre, b_phone)
        markup.row(b_email, b_dni, b_direccion)
        markup.row(b_register, b_unregister)
        markup.row(b_back, b_close)
        return(markup)

    def editUsername(self):
        return("¿Cual es tu usuario?")

    def editPhoto(self):
        return("Envia las fotos que quieras publicar")

    def editName(self):
        return("¿Nombres?")

    def editLastname(self):
        return("¿Apellidos?")

    def editDescription(self):
        return("Escribe una pequeña descripcion")

    def editNationality(self):
        return("¿Cual es tu nacionalidad?")
        # reply = InlineKeyboardMarkup

    def editAge(self):
        return("¿Edad?")

    def editGenre(self):
        return("Sexo")

    def editPhone(self):
        return("Teléfono")

    def editEmail(self):
        return("Email")
        
    def editDNI(self):
        return("DNI")

    def editDireccion(self):
        return("Direccion")

        

    # def editUsername(self):
    #     button = InlineKeyboardMarkup()
    #     buttons_options = {
    #         'cambiar_usuario': InlineKeyboardButton('Nombre publico', callback_data='e_username')
    #         ''
    #     }
    #     pass

handler = profileHandler()