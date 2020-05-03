import telegram, logging

from modules.pytg.ModulesLoader import ModulesLoader

# Form digesters
from .digesters.forms.dummy import dummy_digester

# Request digesters
from .digesters.requests.dummy import dummy_request_digester

def load_digesters():
    # Form digesters
    forms_manager = ModulesLoader.load_manager("forms")

    forms_manager.add_digester("dummy", dummy_digester)

    # Request digesters
    requests_manager = ModulesLoader.load_manager("requests")

    requests_manager.add_digester("dummy", dummy_request_digester)

def initialize():
    logging.info("Initializing various_digesters module...")
    pass

def connect():
    logging.info("Connecting various_digesters module...")

    load_digesters()

def load_manager():
    # There is no need for a manager in this package
    return None

def depends_on():
    return ["bot", "forms", "requests"]