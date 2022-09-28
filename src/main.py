from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from env_manager.manager import EnvManager
from notifier_manager.manager import NotifierManager
from scrapper.sut_scrapper import SutScrapper
from driver_manager import get_driver


def main():
    env_manager = EnvManager(debug=True)
    env_manager.manage()

    notifier_manager = NotifierManager(env_manager)

    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')

        service = Service(get_driver())

        scrapper = SutScrapper(service, env_manager, notifier_manager)
        scrapper.check()

    except Exception as e:
        notifier_manager.send_error_message(str(e))


if __name__ == '__main__':
    main()
