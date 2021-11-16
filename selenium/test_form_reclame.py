import os
import pytest
import allure
from allure_commons.types import AttachmentType
from pages.backend_create_data import BackendCreateData 
from pages.backend_reclame_form import BackendReclameForm
from pages.backend_content_form import BackendContentForm
from pages.frontend_main_page import FrontendMainPage
from pages.frontend_account_page import FrontendAccountPage 
from pages.frontend_reclame_form import FrontendReclameForm 


@pytest.mark.regress
class TestSendAndEditReclameForm():

    @pytest.fixture(scope="function", autouse=True)
    @allure.step("Создать тестовые данные")
    def setup(self, browser):
        '''создать тестовые данные'''
        BCD = BackendCreateData(browser)
        BCD.open()
        BCD.should_login()      # авторизоваться в бэкенде
        BCD.create_test_data()  # создать тестовые данные

    def helper_user_type(self, browser, data):
        with allure.step("Фронтенд - подать заявку на рекламу"):
            FMP = FrontendMainPage(browser)
            FMP.open() 
            FMP.should_open_login_form()            # авторизоваться
            FMP.should_authorized()                 # проверить авторизацию
            FMP.go_to_personal_account()            # зайти в персональный раздел
            FrontendAccountPage(browser).go_to_reclame_form()   # открыть форму подачи заявки на рекламу
            FrontendReclameForm(browser).should_send_form(data) # заполнить данными и отправить
        # бэкенд заявка на рекламу
        with allure.step("Бэкенд - проверить и принять заявку на рекламу"):
            BRreclameF = BackendReclameForm(browser)
            BRreclameF.open()                       # открыть бэкэнд
            BRreclameF.should_be_open_form()        # открыть поданную заявку
            allure.attach(browser.get_screenshot_as_png(), name="BackendReclameForm", attachment_type = AttachmentType.PNG)
            BRreclameF.should_be_right_data(data)   # проверить данные
            BRreclameF.should_moderate_form()       # принять заявку
            BRreclameF.should_be_status('принят, заблокирован') # проверить статус
        # бэкенд контент
        with allure.step("Бэкенд - проверить и опубликовать рекламный контент"):
            BContentF = BackendContentForm(browser)
            BContentF.open()
            BContentF.should_be_open_form()         # открыть форму контента, автоматически созданного
            allure.attach(browser.get_screenshot_as_png(), name="BackendContentForm", attachment_type = AttachmentType.PNG)
            BContentF.should_be_right_data(data)    # проверить данные
            BContentF.unblock_content()             # разблокировать
            BContentF.should_be_unblock()           # и проверить статус контента,
            BRreclameF.should_be_status('принят, опубликован')  # а также статус заявки
    
    @allure.feature("Работа с рекламой")
    @allure.story("Реклама-видео")
    @allure.title("Реклама-видео: от подачи заявки до публикации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_type_video(self, browser):
        ''' тип Видео Youtube '''
        data = {'type': 'Видео Youtube',
                'file': None,
                'link':'https://youtu.be/9Nqk7hqkqbc', 
                'text':'выводимый текст', 
                'views':'1050', 
                'questions':'30',
                'cost': '4230',
                'type_content': 'youtube',
                'code_video': '9Nqk7hqkqbc',
                }
        self.helper_user_type(browser, data)
    
    @allure.feature("Работа с рекламой")
    @allure.story("Реклама-текст")
    @allure.title("Реклама-текст: от подачи заявки до публикации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_type_text(self, browser):
        ''' тип Текст '''
        data = {'type': 'Текст',
                'file': None,
                'link':'https://google.com', 
                'text':'выводимый текст', 
                'views':'1050', 
                'questions':'5',
                'cost': '2105',
                'type_content': 'текст',
                'code_video': '',
                }
        self.helper_user_type(browser, data)

    @allure.feature("Работа с рекламой")
    @allure.story("Реклама-изображение")
    @allure.title("Реклама-изображение: от подачи заявки до публикации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_type_image(self, browser):
        ''' тип Изображение '''
        current_dir = os.path.abspath(os.path.dirname(__file__))
        data = {'type': 'Изображение',
                'file': os.path.join(current_dir, 'file1.jpg'),
                'link':'https://yandex.ru', 
                'text':'выводимый текст', 
                'views':'1050', 
                'questions':'2',
                'cost': '3152',
                'type_content': 'изображение',
                'code_video': '',
                }
        self.helper_user_type(browser, data)
