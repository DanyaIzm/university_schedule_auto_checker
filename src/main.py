from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from driver_manager import get_driver
from env_manager.manager import EnvManager
from error_manager.manager import ErrorManager
from scrapper.sut_scrapper import SutScrapper



def main():
    env_manager = EnvManager(debug=True)
    env_manager.manage()

    try:
        options = webdriver.ChromeOptions()
        # options.add_argument()

        service = Service(get_driver())
        driver = webdriver.Chrome(service=service)

        scrapper = SutScrapper(driver, env_manager)
        scrapper.check()

    except Exception as e:
        ErrorManager(env_manager).send_error_message(str(e))


if __name__ == '__main__':
    main()
