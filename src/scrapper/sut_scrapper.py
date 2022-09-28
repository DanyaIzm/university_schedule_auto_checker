from scrapper.base import BaseScrapper

class SutScrapper(BaseScrapper):
    def __init__(self, driver, env_manager):
        super().__init__(driver, env_manager)

    def check(self):
        pass
