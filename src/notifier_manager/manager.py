import requests


class NotifierManager():
    def __init__(self, env_manager):
        self.env_manager = env_manager

    def send_error_message(self, error):
        message_text = f'При попытке собрать расписание произошла ошибка:\n{error}'
        self._send_message(message_text)

    def send_success_message(self, student_name, lesson_time, lesson_name):
        message_text = f'Успешно отметил {student_name} на паре {lesson_time}: {lesson_name}'
        self._send_message(message_text)

    def send_lesson_not_started_message(self, student_name, lesson_time, lesson_name):
        message_text = f'{student_name} -> преподаватель ещё не начал занятие: {lesson_time}, {lesson_name}'
        self._send_message(message_text)

    def _send_message(self, message_text):
        token = self.env_manager.get_var("TOKEN")
        admin_id = self.env_manager.get_var("ADMIN")

        requests.get(
            f'https://api.telegram.org/bot{token}/sendMessage?chat_id={admin_id}&text={message_text}'
            )
