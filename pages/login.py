import pytest
from selenium import webdriver
from elementium.drivers.se import SeElements
import time


from base.base_page import BasePage
from constants.locators.login_locators import *
from constants.locators.home_page_locators import *
from utils.helper import *
from constants.general_constants import *


class Login(BasePage):
    se = None

    def __init__(self, driver):
        super().__init__(driver)
        self.se = SeElements(driver)
        self.se.navigate(get_correct_url(os.environ["ENV"], 'teacher/login'))

    def load(self):
        self.se.find(NEXT_BUTTON, wait=True)

    def isLoaded(self):
        try:
            assert self.se.find(NEXT_BUTTON, wait=True).is_displayed()
        except wrapping_exceptions():
            raise Error("Page is not loaded properly")

    def get_next_button(self):
        return self.se.find(NEXT_BUTTON, wait=True)

    def get_email_field(self):
        return self.se.find(EMAIL_FIELD, wait=True)

    def type_email(self):
        self.get_email_field().write(EMAIL)

    def get_password_field(self):
        return self.se.find(PASSWORD_FIELD, wait=True)

    def get_welcome_text(self):
        return self.se.find(WELCOME_TEXT, wait=True)

    def type_password(self):
        self.get_password_field().write(PASSWORD)

    def get_login_button(self):
        return self.se.find(LOGIN_BUTTON, wait=True, ttl=3600)

    def click_next_button(self):
        self.get_next_button().click()

    def click_login_button(self):
        self.get_login_button().click()

    def make_login(self):
        self.type_email()
        self.click_next_button()
        self.type_password()
        self.click_login_button()
        self.get_welcome_text()
