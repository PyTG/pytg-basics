import logging, datetime

def dummy_digester(bot, chat_id, form_entries, form_meta):
    logging.info("Dummy digesting ({}, {}, form_meta)".format(chat_id, form_entries, form_meta))

    bot.sendMessage(
        chat_id = chat_id,
        text = "Hello {}!".format(form_entries["name"])
    )

