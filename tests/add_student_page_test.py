from datetime import datetime
import time

from base.base_test import BaseTest
from constants.general_constants import STUDENT_USERNAME, ERROR_MESSAGE
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

    def test_a_add_class_window(self):
        assert self.classpage.get_create_class_button().is_displayed(), "'Create a new class' is not displayed"

    # @pytest.mark.dependency(depends=["test_add_class_window"])
    # @pytest.mark.dependency()
    def test_b_create_class(self):
        self.classpage.click_create_class_button()
        assert self.classpage.get_add_class_window().is_displayed(), "'Add a class' windows is not displayed"
        self.classpage.type_class_name()
        self.classpage.type_grade()
        self.classpage.type_period()
        self.classpage.select_curriculum()
        self.classpage.select_language()
        self.classpage.select_status()
        self.classpage.click_create_class_on_modal()
        assert self.classpage.get_nice_work_text().is_displayed(), "Text is not displayed"


    def test_c_click_add_student(self):
        assert self.classpage.get_add_student().is_displayed(), "Add Student button is not displayed"
        self.classpage.click_add_student()
        assert self.classpage.get_add_student_title().is_displayed(), "Add Student title is not displayed"

    def test_d_create_single_student(self):
        self.classpage.click_add_single_student()
        assert self.classpage.get_student_details().is_displayed(), "Student Details is not displayed"
        assert self.classpage.get_username().is_displayed(), "username is not displayed"
        uname = round(datetime.timestamp(datetime.now()))
        self.classpage.type_username(STUDENT_USERNAME.format(uname))
        assert self.classpage.get_student_password().is_displayed(), "PW does not exist"
        self.classpage.type_student_password()
        assert self.classpage.get_first_name().is_displayed(), "First Name is not displayed"
        self.classpage.type_first_name()
        assert self.classpage.get_last_name().is_displayed(), "Last Name is not displayed"
        self.classpage.type_last_name()
        self.classpage.click_create_student()
        assert self.classpage.get_class_table().is_displayed(), "Table is not displayed"

    def test_e_delete_class(self):
        assert self.classpage.get_checkmark().is_displayed(), "Checkmark is not displayed"
        self.classpage.click_checkmark()
        assert self.classpage.get_bulk_action().is_displayed(), "Bulk Action is not displayed"
        self.classpage.click_bulk_action()
        assert self.classpage.get_delete(), "Delete button is not available"
        self.classpage.click_delete()
        assert self.classpage.get_error_modal().is_displayed(), "Error Modal is not displayed"

    def test_f_error_modal(self):
        assert ERROR_MESSAGE in self.classpage.get_error_text(), "Error message is not corrent"
        assert self.classpage.get_ok_on_error().is_displayed(), "OK button is not displayed"
        self.classpage.click_ok_on_modal()
        assert self.classpage.get_class_table().is_displayed(), "Table is not displayed"