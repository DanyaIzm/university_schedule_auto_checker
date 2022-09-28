# from database import

class BaseScrapper():
    def __init__(self, driver, env_manager, notifier_manager):
        self.driver = driver
        self.env_manager = env_manager
        self.notifier_manager = notifier_manager

    def check(self):
        """
        Checks all students
        """
        
        raise NotImplementedError()
