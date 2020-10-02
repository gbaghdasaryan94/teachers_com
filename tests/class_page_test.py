import pytest

from base.base_test import BaseTest
from pages.login import Login
from pages.class_page import ClassMenu
from constants.general_constants import CLASS_NAME


class TestClassPage(BaseTest):
    loginpage = None
    classpage = None

    def setup_class(cls):
        super().setup_class(cls)
        cls.loginpage = Login(cls.driver).get()
        cls.loginpage.make_login()
        cls.classpage = ClassMenu(cls.driver).get()

    def test_a_select_no_thanks(self, create_class):
        assert self.classpage.get_nice_work_text().is_displayed(), "Text is not displayed"
        assert self.classpage.get_no_thanks().is_displayed(), "'No Thanks' button is not displayed"
        self.classpage.click_no_thanks()
        assert self.classpage.get_class_table().is_displayed(), "Table is not displayed"
        actual_name = self.classpage.get_class_name_inside_table().text()
        assert CLASS_NAME in actual_name, f"Text is not the same, actual text is {actual_name}"
        actual_count = self.classpage.get_student_count().text()
        assert "0" == actual_count, f"Count should be 0, but actual is {actual_count}"

    def test_b_delete_class(self):
        assert self.classpage.get_checkmark().is_displayed(), "Checkmark is not displayed"
        self.classpage.click_checkmark()
        assert self.classpage.get_bulk_action().is_displayed(), "'Bulk Action' is not displayed"
        self.classpage.click_bulk_action()
        assert self.classpage.get_delete(), "'Delete' button is not available"
        self.classpage.click_delete()
        assert self.classpage.get_confirm_field().is_displayed(), "'Confirm' field is not available"
        self.classpage.type_confirm()
        self.classpage.click_ok()
        assert self.classpage.get_create_class_button().is_displayed(), "'Create A New Class' button is not displayed"