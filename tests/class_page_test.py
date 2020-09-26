import time

import pytest
import pytest_dependency

from base.base_test import BaseTest
from pages.login import Login
from pages.class_page import ClassMenu
from constants.general_constants import *


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

    # @pytest.mark.dependency(depends=["test_add_class_window"])
    def test_create_class(self):
        self.classpage.click_create_class_button()
        self.assertTrue(self.classpage.get_add_class_window().is_displayed(), "'Add a class' windows is not displayed")
        self.classpage.type_class_name()
        self.classpage.type_grade()
        self.classpage.type_period()
        self.classpage.select_curriculum()
        self.classpage.select_language()
        self.classpage.select_status()
        self.classpage.click_create_class_on_modal()
        self.assertTrue(self.classpage.get_nice_work_text().is_displayed(), "Text is not displayed")

    def test_select_no_thanks(self):
        self.assertTrue(self.classpage.get_no_thanks().is_displayed(), "'No Thanks' button is not displayed")
        self.classpage.click_no_thanks()
        self.assertTrue(self.classpage.get_class_table().is_displayed(), "Table is not displayed")

    def test_delete_class(self):
        self.classpage.se.refresh()
        self.assertTrue(self.classpage.get_checkmark().is_displayed(), "Checkmark is not displayed")
        self.classpage.click_checkmark()
        self.assertTrue(self.classpage.get_bulk_action().is_displayed(), "Bulk Action is not displayed")
        self.classpage.click_bulk_action()
        self.assertTrue(self.classpage.get_delete(), "Delete button is not available")
        self.classpage.click_delete()
        self.assertTrue(self.classpage.get_confirm_field().is_displayed(), "Confirm field is not available")
        self.classpage.type_confirm()
        self.classpage.send_enter()
        self.assertTrue(self.classpage.get_create_class_button().is_displayed(), "Create A New Class button is not displayed")