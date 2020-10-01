from datetime import datetime
import time

import pytest

from base.base_test import BaseTest
from constants.general_constants import STUDENT_USERNAME, ERROR_MESSAGE, CLASS_NAME
from pages.login import Login
from pages.class_page import ClassMenu


class TestAddStudent(BaseTest):

    loginpage = None
    classpage = None

    def setup_class(cls):
        super().setup_class(cls)
        cls.loginpage = Login(cls.driver).get()
        cls.loginpage.make_login()
        cls.classpage = ClassMenu(cls.driver).get()

    def test_a_create_single_student(self):
        assert self.classpage.get_create_class_button().is_displayed(), "'Create a new class' is not displayed"
        self.classpage.click_create_class_button()
        assert self.classpage.get_add_class_window().is_displayed(), "'Add a class' windows is not displayed"
        self.classpage.type_class_name()
        self.classpage.type_grade()
        self.classpage.type_period()
        self.classpage.select_curriculum()
        self.classpage.select_language()
        self.classpage.select_status()
        self.classpage.click_create_class_on_modal()
        std_count = self.classpage.get_student_count().text()
        assert self.classpage.get_nice_work_text().is_displayed(), "Text is not displayed"
        assert self.classpage.get_add_student().is_displayed(), "Add Student button is not displayed"
        self.classpage.click_add_student()
        assert self.classpage.get_add_student_title().is_displayed(), "Add Student title is not displayed"
        # ADD SINGLE STUDENT
        self.classpage.click_add_single_student()
        assert self.classpage.get_student_details().is_displayed(), "Student Details is not displayed"
        assert self.classpage.get_username().is_displayed(), "'username' is not displayed"
        uname = round(datetime.timestamp(datetime.now()))
        self.classpage.type_username(STUDENT_USERNAME.format(uname))
        assert self.classpage.get_student_password().is_displayed(), "Password filed is not displayed"
        self.classpage.type_student_password()
        assert self.classpage.get_first_name().is_displayed(), "First Name is not displayed"
        self.classpage.type_first_name()
        assert self.classpage.get_last_name().is_displayed(), "Last Name is not displayed"
        self.classpage.type_last_name()
        self.classpage.click_create_student()
        time.sleep(2)
        assert self.classpage.get_class_table().is_displayed(), "Table is not displayed"
        actual_class_name = self.classpage.get_class_name_inside_table().text()
        assert CLASS_NAME in actual_class_name, f"Name is not the same, actual name is {actual_class_name}"
        std_count = self.classpage.get_student_count().text()
        assert "1" == std_count, f"Student Count should be 1, but actual is {std_count}"

    def test_b_delete_class_containing_students(self):
        assert self.classpage.get_checkmark().is_displayed(), "Checkmark is not displayed"
        self.classpage.click_checkmark()
        assert self.classpage.get_bulk_action().is_displayed(), "Bulk Action is not displayed"
        self.classpage.click_bulk_action()
        assert self.classpage.get_delete(), "Delete button is not available"
        self.classpage.click_delete()
        assert self.classpage.get_error_modal().is_displayed(), "Error Modal is not displayed"
        assert ERROR_MESSAGE in self.classpage.get_error_text(), "Error message is not corrent"
        assert self.classpage.get_ok_on_error().is_displayed(), "OK button is not displayed"
        self.classpage.click_ok_on_modal()
