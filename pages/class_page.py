import pytest
from selenium import webdriver
from elementium.drivers.se import SeElements
from selenium.webdriver.common.keys import Keys

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
        return self.se.find_with_wait(CREATE_A_NEW_CLASS)

    def get_add_class_window(self):
        return self.se.find_with_wait(ADD_CLASS_WINDOW)

    def get_class_name(self):
        return self.se.find_with_wait(CLASS_NAME_FIELD)

    def get_grade(self):
        return self.se.find_with_wait(GRADE)

    def get_period(self):
        return self.se.find_with_wait(PERIOD)

    def get_curriculum(self):
        return self.se.find_with_wait(CURRICULUM)

    def get_language(self):
        return self.se.find_with_wait(LANGUAGE)

    def get_status(self):
        return self.se.find_with_wait(STATUS)

    def get_create_class_on_modal(self):
        return self.se.find_with_wait(CREATE_CLASS_ON_MODAL)

    def get_nice_work_text(self):
        return self.se.find_with_wait(NICE_WORK, ttl=10)

    def get_no_thanks(self):
        return self.se.find_with_wait(NO_THANKS)

    def get_class_table(self):
        return self.se.find_with_wait(CLASS_TABLE)

    def get_class_name_inside_table(self):
        return self.se.find_with_wait(CLASS_INSIDE_TABLE).text()

    def get_confirm_field(self):
        return self.se.find_with_wait(CONFIRM_FIELD)

    def get_checkmark(self):
        return self.se.find_with_wait(CLASS_CHECKBOX)

    def get_delete(self):
        return self.se.find_with_wait(CLASS_DELETE)

    def get_bulk_action(self):
        return self.se.find_with_wait(BULK_ACTION)

    def type_class_name(self):
        self.get_class_name().write(CLASS_NAME)

    def type_confirm(self):
        self.get_confirm_field().write(CONFIRM)

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

    def click_checkmark(self):
        self.get_checkmark().click()

    def click_bulk_action(self):
        self.get_bulk_action().click()

    def click_delete(self):
        self.get_delete().click()

    def send_enter(self):
        self.get_confirm_field().write(Keys.ENTER)


