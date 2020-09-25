import time

import pytest
import pytest_dependency
from delayed_assert import expect, assert_expectations

from base.base_test import BaseTest
from pages.login import Login
from pages.class_page import ClassMenu


class TestClassPage(BaseTest):
    loginpage = None
    classpage = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.loginPage = Login(cls.driver).get()
        cls.loginPage.make_login()
        cls.classpage = ClassMenu(cls.driver).get()

    def test_add_class_window(self):
        self.assertTrue(self.classpage.get_create_class_button().is_displayed(), "'Create a new class' is not displayed")
        self.classpage.click_create_class_button()
        self.assertTrue(self.classpage.get_add_class_window().is_displayed(), "'Add a class' windows is not displayed")

    # @pytest.mark.dependency(depends=["test_add_class_window"])
    def test_create_class(self):
        self.classpage.type_class_name()
        self.classpage.type_grade()
        self.classpage.type_period()
        self.classpage.select_curriculum()
        self.classpage.select_language()
        self.classpage.select_status()
        self.classpage.click_create_class_on_modal()

    def test_select_no_thanks(self):
        self.assertTrue(self.classpage.get_no_thanks().is_displayed(), "'No Thanks' button is not displayed")
        self.classpage.click_no_thanks()
        self.assertTrue(self.classpage.get_class_table().is_displayed(), "Table is not displayed")

    def delete_class(self):
        pass