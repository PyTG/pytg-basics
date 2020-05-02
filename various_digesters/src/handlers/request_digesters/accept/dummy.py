import logging

from datetime import datetime

from modules.pytg.ModulesLoader import ModulesLoader

def dummy_accept_digester(bot, chat_id, message_id, request_data):
    logging.info("Dummy accept digesting ({}, {}, {})".format(chat_id, message_id, request_data))