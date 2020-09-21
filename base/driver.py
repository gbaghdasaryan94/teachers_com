from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager


class Driver:
    driver = None

    @classmethod
    def create(cls, browser):
        driver = None
        if browser == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser == "chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser == "edge":
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        elif browser == "IE":
            driver = webdriver.Ie(IEDriverManager().install())
        driver.maximize_window()
        return driver

    def set_driver(self, driver_ins):
        self.driver = driver_ins

    def get_driver(self):
        return self.driver
