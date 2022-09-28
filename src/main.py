from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from env_manager.manager import EnvManager
from error_manager.manager import NotifierManager
from scrapper.sut_scrapper import SutScrapper
from driver_manager import get_driver


def main():
    env_manager = EnvManager(debug=True)
    env_manager.manage()

    notifier_manager = NotifierManager(env_manager)

    try:
        options = webdriver.ChromeOptions()
        # options.add_argument()

        service = Service(get_driver())
        driver = webdriver.Chrome(service=service)

        scrapper = SutScrapper(driver, env_manager, notifier_manager)
        scrapper.check()

    except Exception as e:
        notifier_manager.send_error_message(str(e))


if __name__ == '__main__':
    main()
