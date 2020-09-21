import os
import urllib

import elementium
import selenium
from _csv import Error



def get_correct_url(env, page):
    """
    should return corresponding url for the page based on env variables
    :return:
    """

    return f"{os.environ.get('URL')}/{page}"


def wrapping_exceptions():
    return selenium.common.exceptions.WebDriverException, AssertionError, selenium.common.exceptions.NoSuchElementException, \
           elementium.elements.TimeOutError, \
           TypeError, elementium.exc.TimeOutError, selenium.common.exceptions.UnexpectedTagNameException, AttributeError, \
           selenium.common.exceptions.InvalidSelectorException, urllib.error.URLError, Error
