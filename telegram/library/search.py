import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

response = requests.get('http://localhost:8000/api/users/')
lista = response.json()

class searchHandler:
    def __init__(self):
        self.message = 'Busca resultados <b>cerca a ti</b>\nO <b>personaliza</b> tu busqueda'

    def buttons(self):
        markup = InlineKeyboardMarkup()
        b_searchFilters = InlineKeyboardButton('Personalizar busqueda 📝🔎', callback_data='edit_filtro')
        b_search = InlineKeyboardButton('Buscar 🔎', callback_data='buqueda')
        b_back = InlineKeyboardButton('Volver 🔙', callback_data='start')
        b_close = InlineKeyboardButton("Cerrar 🚪", callback_data="cerrar")
        markup.row(b_searchFilters, b_search)
        markup.row(b_back)
        markup.row(b_close)
        return markup

    def results(self):
        pass

    def profileMessage(self):
        template = ''
        return template

    def profileButtons(self):
        json_input  = ""
        markup = InlineKeyboardMarkup()
        b_whatsapp = InlineKeyboardButton('Envíame un WhatsApp', url=f"https://api.whatsapp.com/send?phone=34{json_input['results'][0]['phone']}")
        b_telegram = InlineKeyboardButton('Envíame un Telegram', url=f"https://t.me/+34{json_input['results'][0]['phone']}")
        b_call = InlineKeyboardButton('Llámame 📞', callback_data='llamame')
        b_reservation = InlineKeyboardButton('Haz una reserva 🗓', callback_data='reservas')
        b_prev = InlineKeyboardButton('⬅️ Anterior', callback_data='anterior')
        b_close = InlineKeyboardButton('❌ Cerrar ❌', callback_data='cerrar')
        b_next = InlineKeyboardButton('Siguiente ➡️', callback_data='siguiente')
        b_back = InlineKeyboardButton('Volver 🔙', callback_data='buscar')
        markup.row(b_whatsapp, b_telegram)
        markup.row(b_call)
        markup.row(b_reservation)
        markup.row(b_prev, b_close, b_next)
        markup.row(b_back)
        return markup

handler = searchHandler()





class profileHandler:
    def __init__(self):
        self.build_url_request()
        self.set_filter_url()
        self.get_json()
        self.init_json_objects_manager()

    def build_url_request(self):
        self.url = "http://localhost:8000/api/users/"

    def set_filter_url(self):
        self.filters = ""
        # by_age = "" if json['age'] else ""
        self.uri = self.url + self.filters

    def get_json(self):
        response = requests.get(self.uri)
        self.json_list = response.json()

    def init_json_objects_manager(self):
        json_length = int(len(self.json_list))
        self.max_index = json_length - 1 if json_length > 0 else 'La busqueda no ha producido ningún resultado'
        self.index = 0
        self.page = self.json_list[self.index]

    def load_current_description(self, json):
        title = f"<b><u>{json['username']}</u></b>\n"
        description = f"{json['description']}\n\n"
        phone = f"<b><u>Telefono:</u></b> {json['phone_prefix']}{json['phone']}\n\n"
        services = "<b><u>Servicios:</u></b>\n"
        for service in json['services']: services += f"\t-{service}\n"
        zone = f"<b>Zona:</b> {json['zone']}"
        self.current_description = title + description + phone + services + zone

    def buttons(self, jsonInput):
        json_input  = jsonInput
        phone = json_input['results'][0]['phone']
        back_page = json_input['previous']
        next_page = json_input['next']
        markup = InlineKeyboardMarkup()
        b_whatsapp = InlineKeyboardButton("Envíame un WhatsApp", url=f"https://api.whatsapp.com/send?phone={phone}")
        b_telegram = InlineKeyboardButton("Envíame un Telegram", url=f"https://t.me/+{phone}")
        b_call = InlineKeyboardButton('Llámame 📞', callback_data='llamame')
        b_reservation = InlineKeyboardButton('Haz una reserva 🗓', callback_data='reservas')
        b_prev = InlineKeyboardButton('⬅️ Anterior', callback_data='anterior')
        b_close = InlineKeyboardButton('❌ Cerrar ❌', callback_data='cerrar')
        b_next = InlineKeyboardButton('Siguiente ➡️', callback_data='siguiente')
        b_back = InlineKeyboardButton('Volver 🔙', callback_data='buscar')
        markup.row(b_whatsapp, b_telegram)
        markup.row(b_call)
        markup.row(b_reservation)
        if back_page is None:
            markup.row(b_close, b_next)
        elif next_page is None:
            markup.row(b_prev, b_close)
        else:
            markup.row(b_prev, b_close, b_next)
        markup.row(b_back)
        return(markup)

    def previous_page(self):
        if self.index == 0:
            self.page = self.json_list[self.index]
        else:
            self.index -= 1
            self.page = self.json_list[self.index]

    def next_page(self):
        if self.index == self.max_index:
            self.page = self.json_list[self.index]
        else:
            self.index += 1
            self.page = self.json_list[self.index]