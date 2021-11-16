import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, TimeoutException 

class BasePage():

    BASE_URL = ""
    CONST_URL = ""

    def __init__(self, browser, url=None, timeout=10):
        self.browser = browser
        self.url = url or self.CONST_URL or ''
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.BASE_URL + self.url)

    def open_url(self, url):
        self.browser.get(self.BASE_URL + url)

    def get_input_checked(self, by_type, by_value):
        el = self.browser.find_element(by_type, by_value)
        return el.get_attribute('checked') is not None

    def get_input_value(self, by_type, by_value):
        el = self.browser.find_element(by_type, by_value)
        return el.get_attribute('value')

    def get_text(self, by_type, by_value):
        el = self.browser.find_element(by_type, by_value)
        return el.text

    def is_element_clickable_with_wait(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until( EC.element_to_be_clickable((how, what)) )
        except TimeoutException:
            return False
        return True


    def is_title_contains_with_wait(self, substring, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until( EC.title_contains(substring) )
        except TimeoutException:
            return False
        return True

    def is_text_in_element_with_wait(self, how, what, text, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until( EC.text_to_be_present_in_element((how, what),text) )
        except TimeoutException:
            return False
        return True
    
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
