import telegram, logging

from datetime import datetime

from modules.pytg.ModulesLoader import ModulesLoader

from telegram.ext import DispatcherHandlerStop

def reply_message_handler(update, context):
    bot = context.bot

    message = update.message

    if not message or not message.chat:
        return

    chat_id = message.chat.id

    username = message.from_user.username
    user_id = message.from_user.id

    text = message.text

    logging.info("Received reply message update from {} ({}) in chat {}: {}".format(username, user_id, chat_id, text))

    # Add an entry and a function for each possible reply menu button
    reply_map = {
        # "Menu": menu,
    }

    if text in reply_map.keys():
        forms_manager = ModulesLoader.load_manager("forms")
        forms_manager.clear_user_form_data(bot, chat_id)

        reply_map[text](bot, chat_id)
