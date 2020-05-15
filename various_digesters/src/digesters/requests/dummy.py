import logging

from datetime import datetime

from modules.pytg.ModulesLoader import ModulesLoader

def dummy_request_digester(bot, chat_id, message_id, request_id, request_data, response):
    logging.info("Dummy request digesting ({}, {}, {}, {}, {})".format(chat_id, message_id, request_id, request_data, response))