import requests
from os import environ

from selenium import webdriver

from driver_manager.manager import get_driver


def main():
    try:
        options = webdriver.ChromeOptions()
        # options.add_argument()

        driver = webdriver.Chrome(get_driver(), options=options)

    except Exception as e:
        message_text = f'При попытке собрать расписание произошла ошибка:\n{e}'

        requests.get(
            f'https://api.telegram.org/bot{environ.get("TOKEN")}/sendMessage?chat_id={environ.get("ADMIN")}&text={message_text}'
            )




if __name__ == '__main__':
    main()
