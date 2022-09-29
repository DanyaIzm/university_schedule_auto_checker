from selenium import webdriver

import schedule
import time

from env_manager.manager import EnvManager
from notifier_manager.manager import NotifierManager
from scrapper.sut_scrapper import SutScrapper
from misc.time_controller import time_control
from service_manager.manager import get_service


def update_service():
    global service
    service = get_service()


@time_control(9, 19)
def main():
    global service

    env_manager = EnvManager()
    env_manager.manage()

    notifier_manager = NotifierManager(env_manager)

    try:
        options = webdriver.ChromeOptions()
        options.binary_location = env_manager.get_var('GOOGLE_CHROME_BIN')
        options.add_argument("--headless")
        options.add_argument('--incognito')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')

        scrapper = SutScrapper(service, options, env_manager, notifier_manager)
        scrapper.check()

    except Exception as e:
        notifier_manager.send_error_message(str(e))


def create_scheduler_tasks():
    schedule.every(1).minutes.do(main)
    schedule.every().day.do(update_service)


def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    # TODO: refactor this (singleton)
    global service
    service = get_service()

    create_scheduler_tasks()
    run_scheduler()
