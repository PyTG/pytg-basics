import telegram, logging

from modules.pytg.ModulesLoader import ModulesLoader

from modules.your_bot_jobs.handlers.jobs.dummy import dummy_job

def schedule_jobs(job_queue):
    job_queue.run_repeating(dummy_job, interval=15*60, first=0)
    pass

def initialize():
    logging.info("Initializing your_bot_jobs module...")
    pass

def connect():
    logging.info("Connecting your_bot_jobs module...")

    bot_manager = ModulesLoader.load_manager("bot")

    schedule_jobs(bot_manager.updater.job_queue)

def load_manager():
    # There is no need for a manager in this package
    return None

def depends_on():
    return ["bot"]
