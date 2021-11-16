import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .settings.locators import FrontendMainPageLocators as Locator
from .settings.config import ConfigFrontend as Config

class FrontendMainPage(BasePage):
    
    BASE_URL = Config.BASE_URL
    CONST_URL = Config.MAIN_PAGE

    @allure.step
    def should_open_login_form(self):
        self.browser.find_element(*Locator.LINK_SIGN).click()
        assert self.is_element_present(*Locator.INPUT_LOGIN), "Фронтенд: поле для ввода логина для авторизации отсутствует"

    @allure.step
    def should_authorized(self):
        # авторизоваться
        self.browser.find_element(*Locator.INPUT_LOGIN).send_keys(Config.USER_LOGIN)
        self.browser.find_element(*Locator.INPUT_PASSWORD).send_keys(Config.USER_PASSWORD)
        self.browser.find_element(*Locator.BUTTON_SIGN).click()
        assert self.is_element_present(*Locator.CHECK_AUTHORIZED), "Фронтенд: пользователь не авторизован"
        assert self.is_element_clickable_with_wait(*Locator.LINK_PERSONAL_ACCOUNT), "Ссылка для перехода в персональный раздел недоступна"
    
    @allure.step
    def go_to_personal_account(self):
        self.browser.find_element(*Locator.LINK_PERSONAL_ACCOUNT).click()
        assert self.is_element_present(*Locator.CHECK_PERSONAL_ACCOUNT), "Фронтенд: персональный раздел не открылся"