from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from driver_manager import get_driver
from error_manager.manager import ErrorManager


def main():
    try:
        options = webdriver.ChromeOptions()
        # options.add_argument()

        service = Service(get_driver())
        driver = webdriver.Chrome(service=service)


    except Exception as e:
        ErrorManager(debug=True).send_erorr_message(str(e))




if __name__ == '__main__':
    main()
