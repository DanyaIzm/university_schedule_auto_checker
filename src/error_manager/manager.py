import requests

from env_manager.manager import EnvManager


class ErrorManager():
    def __init__(self, debug=False):
        self.env_manager = EnvManager(debug=debug)

        self.env_manager.manage()

    def send_erorr_message(self, error):
        message_text = f'При попытке собрать расписание произошла ошибка:\n{error}'
        token = self.env_manager.get_var("TOKEN")
        admin_id = self.env_manager.get_var("ADMIN")

        requests.get(
            f'https://api.telegram.org/bot{token}/sendMessage?chat_id={admin_id}&text={message_text}'
            )
