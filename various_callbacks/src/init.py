import telegram, logging

from modules.pytg.load import manager

from telegram.ext import CallbackQueryHandler

from .handlers.callbacks.dummy import dummy_callback_handler

def load_callback_handlers(dispatcher):
    dispatcher.add_handler(CallbackQueryHandler(dummy_callback_handler, "dummy,*"))

def initialize():
    pass

def connect():
    load_callback_handlers(manager("bot").updater.dispatcher)

def load_manager():
    # There is no need for a manager in this package
    return None

def depends_on():
    return ["bot"]