from dotenv import load_dotenv
from os import path

class EnvManager():
    def __init__(self, debug=False):
        self.debug = debug

    def manage(self):
        if self.debug:
            print(path.join(path.dirname(__file__), '.env'))
            load_dotenv(path.join(path.dirname(__file__), '.env'))
