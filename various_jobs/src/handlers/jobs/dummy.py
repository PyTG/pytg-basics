import telegram, logging, os

from datetime import datetime

from modules.pytg.ModulesLoader import ModulesLoader

def dummy_job(context):
    bot = context.bot

    logging.info("Running dummy job...")