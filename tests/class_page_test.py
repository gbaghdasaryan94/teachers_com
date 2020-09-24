import pytest
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
        self.assertTrue(self.classpage.get_add_class_window().is_displayed(), "'Add a class' windows is not displayed")