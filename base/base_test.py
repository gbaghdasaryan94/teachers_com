import os
import pytest
from base.driver import Driver


class BaseTest():
    driver = None

    def setup_class(cls):
        cls.driver = Driver.create(os.environ["BROWSER"])

    def teardown_class(cls):
        cls.driver.close()

    @pytest.fixture()
    def create_class(self):
        self.classpage.click_create_class_button()
        self.classpage.type_class_name()
        self.classpage.type_grade()
        self.classpage.type_period()
        self.classpage.select_curriculum()
        self.classpage.select_language()
        self.classpage.select_status()
        self.classpage.click_create_class_on_modal()
        return self.classpage.get_nice_work_text()

