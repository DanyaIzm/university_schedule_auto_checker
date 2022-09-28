from dotenv import load_dotenv

from os import path, environ


class EnvManager():
    def __init__(self):
        self.debug = True if not environ.get('DEBUG') else False

    def manage(self):
        if self.debug:
            print(path.join(path.dirname(__file__), '.env'))
            load_dotenv(path.join(path.dirname(__file__), '.env'))

    def get_var(self, name):
        return environ.get(name)
