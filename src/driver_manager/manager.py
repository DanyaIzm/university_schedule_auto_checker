from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    return ChromeDriverManager().install()
