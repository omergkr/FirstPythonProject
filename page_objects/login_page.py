from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.XPATH, "//input[@id='password']")
    __submit_button = (By.CSS_SELECTOR, "button#submit")
    __error_message = (By.XPATH, "//div[@id='error']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__submit_button)

    def get_error_message(self) -> str:
        return super()._get_text(self.__error_message)




