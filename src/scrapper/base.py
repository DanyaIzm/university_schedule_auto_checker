from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions

from env_manager.manager import EnvManager
from notifier_manager.manager import NotifierManager


class BaseScrapper():
    def __init__(self, driver_service: Service, chrome_options: ChromeOptions, env_manager: EnvManager, notifier_manager: NotifierManager):
        self.driver_service = driver_service
        self.chrome_options = chrome_options
        self.env_manager = env_manager
        self.notifier_manager = notifier_manager

    def check(self):
        """
        Checks all students
        """
        
        raise NotImplementedError()
