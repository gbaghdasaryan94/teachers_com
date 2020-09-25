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

    def get_add_class_window(self):
        return self.se.find(ADD_CLASS_WINDOW, wait=True)

    def get_class_name(self):
        return self.se.find(CLASS_NAME_FIELD, wait=True)

    def get_grade(self):
        return self.se.find(GRADE, wait=True)

    def get_period(self):
        return self.se.find(PERIOD, wait=True)

    def get_curriculum(self):
        return self.se.find(CURRICULUM, wait=True)

    def get_language(self):
        return self.se.find(LANGUAGE, wait=True)

    def get_status(self):
        return self.se.find(STATUS,wait=True)

    def get_create_class_on_modal(self):
        return self.se.find(CREATE_CLASS_ON_MODAL, wait=True)

    def get_nice_work_text(self):
        return self.se.find(NICE_WORK, wait=True)

    def get_no_thanks(self):
        return self.se.find(NO_THANKS, wait=True)

    def get_class_table(self):
        return self.se.find(CLASS_TABLE, wait=True)

    def type_class_name(self):
        self.get_class_name().write(CLASS_NAME)

    def click_create_class_button(self):
        self.get_create_class_button().click()

    def type_grade(self):
        self.get_grade().write(GRADE_VALUE)

    def type_period(self):
        self.get_period().write(PERIOD_VALUE)

    def select_curriculum(self):
        self.get_curriculum().select(value=ENGLISH_VALUE)

    def select_language(self):
        self.get_language().select(value=LANGUAGE_VALUE)

    def select_status(self):
        self.get_status().select(value=STATUS_VALUE)

    def click_create_class_on_modal(self):
        self.get_create_class_on_modal().click()

    def click_no_thanks(self):
        self.get_no_thanks().click()

