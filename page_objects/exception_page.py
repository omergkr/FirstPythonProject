from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage


class ExceptionPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button = (By.XPATH, "/html//button[@id='add_btn']")
    __row2_input = (By.XPATH, "(//input[@type='text'])[2]")
    __save_button_row2 = (By.XPATH, "//div[@id='row2']/button[@id='save_btn']")
    __save_button_row1 = (By.XPATH, "//div[@id='row1']/button[@id='save_btn']")
    __confirmation = (By.ID, "confirmation")
    __edit_button = (By.XPATH, "//div[@id='row1']/button[@id='edit_btn']")
    __row1_input = (By.XPATH, "//input[@type= 'text']")
    __instructions = (By.CSS_SELECTOR, "p#instructions")
    __row2_input2 = (By.XPATH, "//div[@id='row2']/input")

    def __int__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def add_row(self):
        super()._click(self.__add_button)

    def type_row2_input(self, text):
        super()._type(self.__row2_input, text)

    def save_row_row2(self):
        super()._click(self.__save_button_row2)

    def save_row_row1(self):
        super()._click(self.__save_button_row1)

    def get_confirmation_text(self) -> str:
        return super()._get_text(self.__confirmation)

    def click_edit_button(self):
        super()._click(self.__edit_button)

    def clear_row1_text(self):
        super()._find(self.__row1_input).clear()

    def type_row1_input(self, text):
        super()._type(self.__row1_input, text)

    def get_row1_attribute(self, value) -> str:
        return super()._find(self.__row1_input).get_attribute(value)

    def get_instructions_text(self) -> str:
        return super()._get_text(self.__instructions)

    def is_invisibility_instructions(self) -> bool:
        wait = WebDriverWait(self._driver, 10)

        try:
            wait.until(EC.invisibility_of_element_located(
                self.__instructions)), "Instruction text element should not be displayed"
            return True
        except NoSuchElementException:
            return False

    def row2_input_is_displayed(self):
        super()._is_displayed(self.__row2_input2)
