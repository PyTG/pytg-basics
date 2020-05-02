import logging, datetime

def dummy_digester(bot, form_entries, user_data):
    logging.info("Dummy digesting ({}, {})".format(user_data["chat_id"], form_entries))

    bot.sendMessage(
        chat_id = user_data["chat_id"],
        text = "Hello {}!".format(form_entries["name"])
    )

