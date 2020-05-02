import logging, datetime

from modules.pytg.ModulesLoader import ModulesLoader

def dummy_reject_digester(bot, chat_id, message_id, request_data):
    logging.info("Dummy reject digesting ({})".format(chat_id, message_id, request_data))