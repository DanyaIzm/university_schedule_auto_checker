from selenium.webdriver.chrome.service import Service

from env_manager.manager import EnvManager
from notifier_manager.manager import NotifierManager


class BaseScrapper():
    def __init__(self, driver_service: Service, env_manager: EnvManager, notifier_manager: NotifierManager):
        self.driver_service = driver_service
        self.env_manager = env_manager
        self.notifier_manager = notifier_manager

    def check(self):
        """
        Checks all students
        """
        
        raise NotImplementedError()
