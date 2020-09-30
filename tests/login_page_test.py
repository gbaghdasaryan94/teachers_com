import pytest

from base.base_test import BaseTest
from pages.login import Login


class TestLoginPage(BaseTest):
    loginPage = None

    @classmethod
    def setup_class(cls):
        super().setup_class(cls)
        cls.loginPage = Login(cls.driver).get()
        cls.loginPage.make_login()

    def test_check_login_functionality(self):
        assert (self.loginPage.get_next_button().is_displayed(), "'Next' button is not displayed")