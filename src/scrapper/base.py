# from database import

class BaseScrapper():
    def __init__(self, driver, database_manager):
        self.driver = driver
        self.database_manager = database_manager

    def scrap_and_save(self):
        """
        Scraps the schedule of all students in the database and saves it to the database
        """
        
        raise NotImplementedError()
