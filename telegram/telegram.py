import telebot
from library import start, search, unregister, register, profiles


class botHandler:
    def __init__(self):
        TOKEN = '5924131606:AAF260YSrBRNqEme3ucNIUVkpBUMLSYtWFs'
        self.bot = telebot.TeleBot(TOKEN, parse_mode="html")
        self.callbackQueryHandler()
        self.commands()

    def callbackQueryHandler(self):
        @self.bot.callback_query_handler(func=lambda x: True)
        def handlerButtons(call):
            cid = call.from_user.id
            mid = call.message.id
            cad = call.data

            # Handler START
            if cad == "start":
                self.homePage(mid, cid)

            # Handler CERRAR
            if cad == "cerrar":
                self.bot.delete_message(cid, mid)

            # Handler ANTERIOR
            if cad == "anterior":
                self.bot.delete_message(cid, mid)

            # Handler SIGUIENTE
            if cad == "siguiente":
                self.bot.delete_message(cid, mid)

            # Handler BUSQUEDA
            if cad == "buscar":
                self.bot.edit_message_text(
                    search.handler.message, cid, mid, reply_markup=search.handler.buttons())

            # Handler PERFIL
            if cad == "perfil":
                self.bot.edit_message_text(
                    profiles.handler.message, cid, mid, reply_markup=profiles.handler.buttons())

            # Handler ALTA
            if cad == "alta":
                self.bot.edit_message_text(
                    register.message, cid, mid, reply_markup=register.buttons())

            # Handler BAJA
            if cad == "baja":
                self.bot.edit_message_text(
                    unregister.message, cid, mid, reply_markup=unregister.buttons())

        # Comandos del bot
    def commands(self):
        @self.bot.message_handler(commands=['start'])
        def cmd_start(message):
            self.homePage(message.chat.id)

        @self.bot.message_handler(commands=['help', 'ayuda'])
        def cmd_help(message):
            self.homePage(message.chat.id, help_cmd=True)

    def homePage(self, mid, cid=None, help_cmd=None):
        if help_cmd is True:
            return(self.bot.send_message(mid, start.help, reply_markup=start.buttons()))
        if cid is None:
            return(self.bot.send_message(mid, start.welcome, reply_markup=start.buttons()))
        else:
            return(self.bot.edit_message_text(start.help, cid, mid, reply_markup=start.buttons()))

    def searchHandler(self):
        pass

    @classmethod
    def runBot(cls):
        self = cls()
        print("Iniciando bot...")
        self.bot.infinity_polling()

if __name__ == '__main__':
    botHandler().runBot()
