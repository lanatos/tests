import allure
from .base_page import BasePage
from .settings.locators import BackendCreateDataLocators as Locator
from .settings.config import ConfigBackend as Config

class BackendCreateData(BasePage):

    BASE_URL = Config.BASE_URL
    CONST_URL = Config.MAIN_PAGE
    CREATE_DATA_URL = Config.CREATE_DATA_URL

    @allure.step
    def should_login(self):
        self.browser.find_element(*Locator.INPUT_LOGIN).send_keys(Config.USER_LOGIN)
        self.browser.find_element(*Locator.INPUT_PASSWORD).send_keys(Config.USER_PASSWORD)
        self.browser.find_element(*Locator.BUTTON_SIGN).click()
        assert self.is_element_present(*Locator.CHECK_AUTHORIZED), "Бэкэнд: пользователь не авторизован"

    @allure.step
    def create_test_data(self):
        self.browser.get(self.BASE_URL + self.CREATE_DATA_URL)
        assert self.is_element_present(*Locator.CHECK_CREATED_DATA), "Бэкэнд: тестовые данные не созданы"