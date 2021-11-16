import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .settings.locators import FrontendReclameFormLocators as Locator
from .settings.config import ConfigFrontend as Config

class FrontendReclameForm(BasePage):
    
    BASE_URL = Config.BASE_URL
    CONST_URL = Config.ACCOUNT_PAGE

    def get_message_error(self):
        try:
            error = self.browser.find_element(*Locator.FORM_MESSAGE_ERROR)
            return error.text
        except:
            return ''

    def fill_main_fields(self,data):
        # заполнить основными данными
        scroll_up = self.browser.find_element(*Locator.FORM_TYPE_CONTENT_UP)
        self.browser.find_element(*Locator.FORM_TYPE_CONTENT).click() # тип Видео Youtube
        if data['type'] == 'Видео Youtube':
            scroll_up.click()
        elif data['type'] == 'Изображение':
            # пролистать до типа видео
            #assert self.is_element_present(*Locator.FORM_ADD_IMAGE)
            self.browser.find_element(*Locator.FORM_ADD_IMAGE).send_keys(data['file'])
        elif data['type'] == 'Текст':
            # пролистать до типа текст
            scroll_up.click()
            scroll_up.click()
        self.browser.find_element(*Locator.FORM_LINK_PAGE).send_keys(data['link']) 
        self.browser.find_element(*Locator.FORM_TEXT).send_keys(data['text']) 
        self.browser.find_element(*Locator.FORM_TEXT_COLOR).click()
        self.browser.find_element(*Locator.FORM_VIEWS).send_keys(data['views']) 
        self.browser.find_element(*Locator.FORM_QUESTIONS).send_keys(data['questions']) 

    @allure.step
    def should_send_form(self, data):
        self.fill_main_fields(data)
        self.browser.find_element(*Locator.FORM_SUBMIT).click() # отправить
        assert self.is_element_present(*Locator.CHECK_FORM_CLOSED), "Фронтенд: " \
            "форма не отправилась, сообщение об ошибке: {}".format(self.get_message_error())