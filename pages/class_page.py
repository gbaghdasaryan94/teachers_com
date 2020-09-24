import pytest
from selenium import webdriver
from elementium.drivers.se import SeElements


from base.base_page import BasePage
from constants.locators.class_page_locators import *
from utils.helper import *
from constants.general_constants import *


class ClassMenu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.se = SeElements(driver)
        self.se.navigate(get_correct_url(os.environ["ENV"], 'teacher/classes'))

    def load(self):
        self.se.find(CREATE_A_NEW_CLASS, wait=True)

    def isLoaded(self):
        try:
            assert self.se.find(CREATE_A_NEW_CLASS, wait=True).is_displayed()
        except wrapping_exceptions():
            raise Error("Page is not loaded properly")

    def get_create_class_button(self):
        return self.se.find(CREATE_A_NEW_CLASS, wait=True)

    def click_create_class_button(self):
        self.get_create_class_button().click()

    def get_add_class_window(self):
        return self.se.find(ADD_CLASS_WINDOW, wait=True)

