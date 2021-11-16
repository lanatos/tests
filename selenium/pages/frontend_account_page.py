import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .settings.locators import FrontendAccountPageLocators as Locator
from .settings.config import ConfigFrontend as Config

class FrontendAccountPage(BasePage):
    
    BASE_URL = Config.BASE_URL
    CONST_URL = Config.ACCOUNT_PAGE
    
    @allure.step
    def go_to_reclame_form(self):
        self.browser.find_element(*Locator.LINK_RECLAME_FORM).click()
        assert self.is_element_present(*Locator.CHECK_RECLAME_FORM), "Фронтенд: форма для подачи рекламы не открыта"