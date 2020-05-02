import telegram, logging

from modules.pytg.ModulesLoader import ModulesLoader

from telegram.ext import MessageHandler, Filters

from modules.your_bot_messages.handlers.messages.reply import reply_message_handler

def load_messages_handlers(dispatcher):
    module_id = ModulesLoader.get_module_id("your_bot_messages")

    dispatcher.add_handler(MessageHandler(Filters.text, reply_message_handler), group=module_id)

def initialize():
    logging.info("Initializing your_bot_messages module...")
    pass

def connect():
    logging.info("Connecting your_bot_messages module...")

    bot_manager = ModulesLoader.load_manager("bot")

    load_messages_handlers(bot_manager.updater.dispatcher)

def load_manager():
    # There is no need for a manager in this package
    return None

def depends_on():
    return ["bot", "data", "text", "menu", "forms"]