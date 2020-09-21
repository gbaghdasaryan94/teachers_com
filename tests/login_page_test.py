import pytest
from delayed_assert import expect, assert_expectations

from base.base_test import BaseTest
from pages.login import Login


class TestLoginPage(BaseTest):
    loginPage = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.loginPage = Login(cls.driver).get()


    def test_check_login_functionality(self):
        self.assertTrue(self.loginPage.get_next_button().is_displayed(), "'Next' button is not displayed")