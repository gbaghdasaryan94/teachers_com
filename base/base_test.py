import os
import pytest
from base.driver import Driver


class BaseTest():
    driver = None

    def setup_class(cls):
        cls.driver = Driver.create(os.environ["BROWSER"])

    def teardown_class(cls):
        cls.driver.close()

