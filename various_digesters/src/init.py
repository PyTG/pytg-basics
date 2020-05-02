import telegram, logging

from modules.pytg.ModulesLoader import ModulesLoader

# Form digesters
from modules.your_bot_digesters.handlers.form_digesters.dummy import dummy_digester

# Request digesters
from modules.your_bot_digesters.handlers.request_digesters.accept.dummy import dummy_accept_digester
from modules.your_bot_digesters.handlers.request_digesters.reject.dummy import dummy_reject_digester

def load_digesters():
    # Form digesters
    forms_manager = ModulesLoader.load_manager("forms")

    forms_manager.add_digester("dummy", dummy_digester)

    # Request digesters
    requests_manager = ModulesLoader.load_manager("requests")

    requests_manager.add_digester("dummy", dummy_accept_digester, dummy_reject_digester)

def initialize():
    logging.info("Initializing your_bot_digesters module...")
    pass

def connect():
    logging.info("Connecting your_bot_digesters module...")

    load_digesters()

def load_manager():
    # There is no need for a manager in this package
    return None

def depends_on():
    return ["bot", "forms", "requests"]