import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .settings.locators import BackendReclameFormLocators as Locator
from .settings.config import ConfigBackend as Config

class BackendReclameForm(BasePage):
    
    BASE_URL = Config.BASE_URL
    CONST_URL = Config.UPDATE_RECLAME

    def open_list(self):
        self.open_url(Config.MANAGE_RECLAME)

    @allure.step
    def should_be_open_form(self):
        assert self.is_element_present(*Locator.CHECK_RECLAME_FORM), \
            "Backend_reclame_form: форма заявки на рекламу не открывается"

    @allure.step
    def should_be_right_data(self,data):
        rows = self.browser.find_elements(*Locator.FORM_FIELDS)
        assert rows[0].text == '1', "Backend_reclame_form: поле id пользователя некорректно"
        assert rows[2].text == data['type'], "Backend_reclame_form: поле Вид рекламы некорректно"
        assert rows[3].text == data['link'], "Backend_reclame_form: поле Ссылка некорректно"
        assert rows[4].text == data['text'], "Backend_reclame_form: поле Выводимый текст Рекламы некорректно"
        assert rows[5].text.strip() == 'ffff66', f"Backend_reclame_form: поле Цвет некорректно: {rows[5].text}"
        assert rows[6].text == data['views'], "Backend_reclame_form: поле Количество выводов некорректно"
        assert rows[7].text == data['questions'], "Backend_reclame_form: поле Количество вопросов некорректно"
        assert rows[8].text == data['cost'], f"Backend_reclame_form: поле Стоимость услуги некорректно: {rows[8].text}"
        assert rows[9].text == 'заявка подана', "Backend_reclame_form: поле Статус некорректно"
        assert rows[10].text == '(не задано)', "Backend_reclame_form: поле Дата модерации некорректно"
        if data['type'] == 'Backend_reclame_form: Изображение':
            assert self.is_element_present(*Locator.FORM_INFO_IMG), "Backend_reclame_form: Изображение отсутствует"

    def get_status_reclame(self):
        rows = self.browser.find_elements(*Locator.FORM_FIELDS)
        return rows[9].text

    @allure.step
    def should_moderate_form(self):
        self.browser.find_element(*Locator.FORM_BUTTON_UPDATE).click() # отправить
        assert self.is_element_present(*Locator.CHECK_FORM_CLOSED), \
            "Backend_reclame_form: ошибка при сохранении формы"
    
    @allure.step
    def should_be_status(self, status):
        self.browser.get(self.BASE_URL + Config.UPDATE_RECLAME)
        assert self.get_status_reclame() == status, \
            f"Backend_reclame_form: статус заявки на рекламу должен быть {status}"