from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from driver_manager import get_driver
from error_manager.manager import ErrorManager
from scrapper.sut_scrapper import SutScrapper



def main():
    try:
        options = webdriver.ChromeOptions()
        # options.add_argument()

        service = Service(get_driver())
        driver = webdriver.Chrome(service=service)

        scrapper = SutScrapper(driver, ...)
        scrapper.scrap_and_save()

    except Exception as e:
        ErrorManager(debug=True).send_erorr_message(str(e))


if __name__ == '__main__':
    main()
