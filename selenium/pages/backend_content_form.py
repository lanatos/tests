import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .settings.locators import BackendContentFormLocators as Locator
from .settings.config import ConfigBackend as Config

class BackendContentForm(BasePage):
    
    BASE_URL = Config.BASE_URL
    CONST_URL = Config.UPDATE_CONTENT

    FORM_TEXT = (By.CSS_SELECTOR, "#content-textmin")
    FORM_VIEWS_BEGIN = (By.CSS_SELECTOR, "#content-count_begin")
    FORM_VIEWS_LOST = (By.CSS_SELECTOR, "#content-count_lost")
    FORM_COUNT_QUESTIONS = (By.CSS_SELECTOR, ".grid-view table tr")
    FORM_SUBMIT = (By.CSS_SELECTOR, "#b-save")
    CHECK_FORM_CLOSED = (By.XPATH, '.content-index')

    def open_list(self):
        self.open_url(Config.MANAGE_CONTENT)

    @allure.step
    def should_be_open_form(self):
        assert self.is_element_present(*Locator.CHECK_CONTENT_FORM), \
            "Backend_content_form: форма контента не открывается"

    @allure.step
    def should_be_right_data(self, data):
        assert self.get_input_value(*Locator.FORM_NAME) == 'Заявка 1', \
            "Backend_content_form: поле Наименование некорректно"
        assert self.get_text(*Locator.FORM_TYPE_CONTENT) == data['type_content'], \
            "Backend_content_form: поле Тип контента некорректно"
        if data['type'] == 'Видео Youtube':
            assert self.get_input_value(*Locator.FORM_VIDEO) == data['code_video'], \
                "Backend_content_form: поле Код видео некорректно"
        assert self.get_input_value(*Locator.FORM_LINK_PAGE) == data['link'], \
            "Backend_content_form: поле Ссылка на страницу некорректно"
        assert self.get_input_checked(*Locator.FORM_BLOCKED), \
            "Backend_content_form: поле Блокировна некорректно"
        if data['type'] == 'Текст':
            text = self.browser.execute_script("return $('.cleditorMain #content-text').html();") 
            assert text == data['text'], \
                "Backend_content_form: поле Текст некорректно"
        else:
            assert self.get_text(*Locator.FORM_TEXT) == data['text'], \
                "Backend_content_form: поле Текст некорректно"
        assert self.get_input_value(*Locator.FORM_VIEWS_BEGIN) == data['views'], \
            "Backend_content_form: поле Начальное количество просмотров некорректно"
        assert self.get_input_value(*Locator.FORM_VIEWS_LOST) == data['views'], \
            "Backend_content_form: поле Оставшееся количество просмотров некорректно"
        rows = self.browser.find_elements(*Locator.FORM_COUNT_QUESTIONS)
        assert str(len(rows)-1) == data['questions'], \
            "Backend_content_form: количество созданных вопросов некорректно"
        if data['type'] == 'Изображение':
            assert self.is_element_present(*Locator.FORM_INFO_IMG), "Backend_content_form: Изображение отсутствует"
        
    @allure.step
    def unblock_content(self):
        self.browser.find_element(*Locator.FORM_BLOCKED).click()
        self.browser.find_element(*Locator.FORM_SUBMIT).click()
        assert self.is_title_contains_with_wait('updated'), \
            f"Backend_content_form: сохранение формы не успешно {self.browser.title}"

    @allure.step
    def should_be_unblock(self):
        self.browser.find_element(*Locator.FORM_CLOSE).click()
        assert self.is_element_present(*Locator.CHECK_FORM_CLOSED), \
            "Backend_content_form: список контента не открылся"
        rows = self.browser.find_elements(*Locator.LIST_CHECKBOX)
        assert rows[1].get_attribute('checked') is None, \
            f"Backend_content_form: Блокировка контента не снята {rows[1].get_attribute('checked')}"

