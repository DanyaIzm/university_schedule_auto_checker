import requests


class NotifierManager():
    def __init__(self, env_manager):
        self.env_manager = env_manager

    def send_error_message(self, error):
        message_text = f'При попытке собрать расписание произошла ошибка:\n{error}'
        token = self.env_manager.get_var("TOKEN")
        admin_id = self.env_manager.get_var("ADMIN")

        requests.get(
            f'https://api.telegram.org/bot{token}/sendMessage?chat_id={admin_id}&text={message_text}'
            )
