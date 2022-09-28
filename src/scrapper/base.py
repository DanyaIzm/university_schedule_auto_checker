# from database import

class BaseScrapper():
    def __init__(self, driver, env_manager):
        self.driver = driver
        self.env_manager = env_manager

    def check(self):
        """
        Checks all students
        """
        
        raise NotImplementedError()
