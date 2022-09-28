import requests

from os import environ

from env_manager.manager import EnvManager


class ErrorManager():
    def __init__(self, debug=False):
        EnvManager(debug=debug).manage()

    def send_erorr_message(self, error):
        message_text = f'При попытке собрать расписание произошла ошибка:\n{error}'

        requests.get(
            f'https://api.telegram.org/bot{environ.get("TOKEN")}/sendMessage?chat_id={environ.get("ADMIN")}&text={message_text}'
            )
