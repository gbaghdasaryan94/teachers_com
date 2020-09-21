import unittest
from base.driver import Driver


class BaseTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver.create('chrome')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

