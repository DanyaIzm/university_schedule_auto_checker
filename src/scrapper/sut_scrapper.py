from scrapper.base import BaseScrapper

class SutScrapper(BaseScrapper):
    def __init__(self, driver, database_manager):
        super().__init__(driver, database_manager)

    def scrap_and_save(self):
        pass
