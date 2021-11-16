from selenium.webdriver.common.by import By

class BackendCreateDataLocators():
    INPUT_LOGIN = (By.CSS_SELECTOR, "#loginform-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#loginform-password")
    BUTTON_SIGN = (By.CSS_SELECTOR, "button[name='login-button']")
    CHECK_AUTHORIZED = (By.CSS_SELECTOR, "#planallcount")
    CHECK_CREATED_DATA = (By.CSS_SELECTOR, "#created")

class BackendReclameFormLocators():
    CHECK_RECLAME_FORM = (By.CSS_SELECTOR, ".contentz-update")
    FORM_FIELDS = (By.CSS_SELECTOR, ".contentz-form td")
    FORM_INFO_IMG = (By.CSS_SELECTOR, "#imgcontent")
    FORM_BUTTON_UPDATE = (By.CSS_SELECTOR, ".contentz-form #divcol1 button")
    CHECK_FORM_CLOSED = (By.CSS_SELECTOR, '.reklama-index')

class BackendContentFormLocators():
    CHECK_CONTENT_FORM = (By.CSS_SELECTOR, ".content-update")
    FORM_NAME = (By.CSS_SELECTOR, "#content-name")
    FORM_TYPE_CONTENT = (By.CSS_SELECTOR, "#content-vid option[selected]")
    FORM_VIDEO = (By.CSS_SELECTOR, "#content-video")
    FORM_LINK_PAGE = (By.CSS_SELECTOR, "#content-url")
    FORM_BLOCKED = (By.CSS_SELECTOR, "#content-block")
    FORM_TEXT = (By.CSS_SELECTOR, "#content-textmin")
    FORM_TEXT2 = (By.CSS_SELECTOR, ".cleditorMain #content-text")
    FORM_VIEWS_BEGIN = (By.CSS_SELECTOR, "#content-count_begin")
    FORM_VIEWS_LOST = (By.CSS_SELECTOR, "#content-count_lost")
    FORM_COUNT_QUESTIONS = (By.CSS_SELECTOR, ".grid-view table tr")
    FORM_SUBMIT = (By.CSS_SELECTOR, "#b-save")
    FORM_CLOSE = (By.CSS_SELECTOR, "#b-bclose")
    CHECK_FORM_CLOSED = (By.CSS_SELECTOR, '.content-index')
    LIST_CHECKBOX = (By.CSS_SELECTOR, "input[type=checkbox]")
    FORM_INFO_IMG = (By.CSS_SELECTOR, ".rightimage")


class FrontendMainPageLocators():
    LINK_SIGN = (By.CSS_SELECTOR, "#sotmenu6")
    INPUT_LOGIN = (By.CSS_SELECTOR, "input#login")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input#pass")
    BUTTON_SIGN = (By.CSS_SELECTOR, "button#enter")
    CHECK_AUTHORIZED = (By.CSS_SELECTOR, ".b-flipper-panel")
    LINK_PERSONAL_ACCOUNT = (By.CSS_SELECTOR, ".e-project")
    CHECK_PERSONAL_ACCOUNT = (By.CSS_SELECTOR, ".b-left-icons-dob .i-stat")

class FrontendAccountPageLocators():
    LINK_RECLAME_FORM = (By.CSS_SELECTOR, ".i-reklama")
    CHECK_RECLAME_FORM = (By.CSS_SELECTOR, "#showcontent")

class FrontendReclameFormLocators():
    FORM_TYPE_CONTENT = (By.CSS_SELECTOR, "#showcontent #labelformat")
    FORM_TYPE_CONTENT_UP = (By.CSS_SELECTOR, "#showcontent #format_up")
    FORM_TYPE_CONTENT_DOWN = (By.CSS_SELECTOR, "#showcontent #format_up")
    FORM_ADD_IMAGE = (By.CSS_SELECTOR, "#contentimage")
    FORM_LINK_PAGE = (By.CSS_SELECTOR, "#showcontent #fieldurl")
    FORM_TEXT = (By.CSS_SELECTOR, "#showcontent #contentinfo")
    FORM_TEXT_COLOR = (By.CSS_SELECTOR, "#showcontent #content_c3")
    FORM_VIEWS = (By.CSS_SELECTOR, "#showcontent #typepar")
    FORM_QUESTIONS = (By.CSS_SELECTOR, "#showcontent #dayspar")
    FORM_SUBMIT = (By.CSS_SELECTOR, "#b-left2 .a_sendcontent")
    CHECK_FORM_CLOSED = (By.XPATH, '//div[@id="changes" and @style="display: none; opacity: 1;"]')
    FORM_MESSAGE_ERROR = (By.CSS_SELECTOR, "#form-message")
