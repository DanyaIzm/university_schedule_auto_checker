from selenium.webdriver.chrome.service import Service

from driver_manager import get_driver


def get_service() -> Service:
    return Service(get_driver())
