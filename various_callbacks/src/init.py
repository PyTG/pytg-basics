import telegram, logging

from modules.pytg.ModulesLoader import ModulesLoader

from telegram.ext import CallbackQueryHandler

def load_callback_handlers(dispatcher):
    pass

def initialize():
    logging.info("Initializing your_bot_callbacks module...")
    pass

def connect():
    logging.info("Connecting your_bot_callbacks module...")

    bot_manager = ModulesLoader.load_manager("bot")

    load_callback_handlers(bot_manager.updater.dispatcher)

def load_manager():
    # There is no need for a manager in this package
    return None

def depends_on():
    return ["bot"]