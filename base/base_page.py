from utils.helper import wrapping_exceptions


class BasePage:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        """
        should wait specific element of the page
        :return:
        """


    def isLoaded(self):
        """
        Check if that specific element exist
        :return: Throw Exception if the element is missing
        """
        pass

    def get(self):
        """
        Checks if the page is loaded successfully
        :return: page object
        """
        try:
            self.isLoaded()
            return self
        except wrapping_exceptions() as err:
            self.load()
            self.isLoaded()
            return self

    def get_driver(self):
        return self.driver
